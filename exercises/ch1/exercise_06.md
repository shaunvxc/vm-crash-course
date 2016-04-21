# Machine #6

**Goal**: Extend [Machine 5](exercise_05.md) with "static calls" and a linking phase.

### Instruction format

For this machine, our `operation` size will be smaller to make room for `operand`s of bigger size.

Let:

- Word size: `sizeof(void*)` bits
- operation: `8` bits
- operand: `sizeof(void*)-8` bits

Instruction format: `[ operation | operand ]`

All instructions are `sizeof(void*)` bits long, even if the operation does not have arguments (in that case, operand should be ignored).

### Instruction set

This machine introduces changes to the semantics of `CALL`:


- `PUSH <ARG>`: 0x1
- `POP`:  0x2
- `SUM`:  0x3
- `SUMX`: 0x4
- `PCALL <ID>`: 0x5
- `CALL <addr>`: 0x6

  `CALL <addr>` transfers the execution to the user-defined subroutine in
  memory address `addr`. When the subroutine finishes execution, it's
  resulting value should be at the top of the stack.

- `RET`: 0x7
- `PUSH_ARG <ARG>`: 0x8

### Machine memory

The same as `Machine #5`

### Programs


A program for `Machine #6` has similar format of programs for `Machine #5`
with two slight differences in the `header`.

#### header

A header is divided in:

```
[ main_addr                : word-size bits]
[ reloc_table_size         : word-size bits]
[ reloc_addr#1             : word-size bits]
[ reloc_addr#2             : word-size bits]
[ ...                                      ]
[ reloc_addr#N             : word-size bits]
```

The `main_addr` is the offset in the program where the main procedure starts -- the position of the first `main` instruction in the object file.

The `reloc_table_size` indicates the number of entries `N` in the relocation
table. Each entry following this number is an addresses (`base`d on the object
file) inside the `body` section that should be recalculated.

Specifically, each `addr` from `CALL` instructions in the `body` should be
pointed by a `reloc_addr`.

For example, if the `body` of the program contains two `CALL` instructions:

```
0xCC: CALL 0x30
...
0xFB: CALL 0xC2
...
```

Then, the header should contain two `reloc_addr` entries, one with the value
`0xCC` and another with `0xFB`:

```
                //header
0x0: 0xABC      //main_addr
0x1: 2          //reloc_table_size
0x2: 0xCC       //reloc_addr#1
0x3: 0xFB       //reloc_addr#2
....            //begin body...
0xCC: CALL 0x30
...
0xFB: CALL 0xC2
...
```


#### body

The `body` of a program is just a concatenation of user-defined subroutine
bodies -- a subroutine body is just a string of instructions.

All subroutine bodies should end with `RET <VAL>` instruction.


### Loading and linking programs

Upon loading the program in memory, the VM should update all `CALL` operands
(`addr`) to valid memory pointers.

For example, consider the following program object loaded in memory:

```
0xDE3: 0xABC      //main_addr
0xDE4: 2          //reloc_table_size
0xDE5: 0xCC       //reloc_addr#1
0xDE6: 0xFB       //reloc_addr#2
....              //begin body...
0xEAF: CALL 0x30
...
0xEBE: CALL 0xC2
...
```


For each `reloc_addr#N` in the relocation table, the VM should:

- obtain the address `ADDR` of the entry `reloc_addr#N` (e.g. `0xCC`)

- deference `*ADDR+base`, where base is the beginning of the program in memory
 (e.g. `0xCC+0xDE3`, which is `0xEAF`) to reach the `CALL` instruction.

- Rewrite the call operand with its value + `base` (e.g. `0x30+0xDE3` is
  `0xE13`, thus, `CALL 0x30` becomes `CALL 0xE13`) -- if the resulting value
  exceeds the `operand` size, the VM should exit with an error.

Upon processing the relocation table, the resulting code should be:

```
0xDE3: 0xABC      //main_addr
0xDE4: 2          //reloc_table_size
0xDE5: 0xFA       //reloc_addr#1
0xDE6: 0x2B       //reloc_addr#2
....              //begin body...
0xEDD: CALL 0xE13
...
0xE0E: CALL 0xEA5
...
```

### Execution

The same as `Machine #5`. After loading & linking a program, the
VM should lookup the `main` entry in the object file by following the
`header`'s `main_addr`. Upon finding such entry, the VM should start executing
the code pointed by it.

### Usage

Same as `Machine #5`.
