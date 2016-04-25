# Machine #8

**Goal**: Extend [Machine 7](../ch1/exercise_07.md) with support for "big ints".

In a machine where `sizeof(void*)` is 64 bits, the total bits available for an
operand is 56 bits (see "Instruction format" section below). Thus, so far, the
biggest (unsigned) integer that can be operated with `PUSH` and `SUM` is
72057594037927935. This machine introduces support for operating integers of
`sizeof(void*)`.

The rest of this documents assumes `sizeof(void*)` is  64 bits.

### Instruction format

The same as `Machine #7`:

Let:

- Word size: `sizeof(void*)` bits
- operation: `8` bits
- operand: `sizeof(void*)-8` bits

Instruction format: `[ operation | operand ]`

All instructions are `sizeof(void*)` bits long, even if the operation does not have arguments (in that case, operand should be ignored).

 ### Instruction set

This machine introduces `PUSH_DATA` and `BIG_SUM`:


- `PUSH <ARG>`: 0x1
- `POP`:  0x2
- `SUM`:  0x3
- `SUMX`: 0x4
- `PCALL <ID>`: 0x5
- `CALL <addr>`: 0x6
- `RET`: 0x7
- `PUSH_ARG <ARG>`: 0x8
- `INC_SP <ARG>`: 0x9
- `PUSH_LOCAl <ARG>`: 0xA
- `POP_LOCAl <ARG>`: 0xB
- `PUSH_DATA <addr>`: 0xC

   Pushes the address `addr` (i.e. within `data` section, see below) on the stack.

- `BIG_SUM`: 0xD

  Pops and sums the 2 topmost values on the stack. These values should be
  pointers to two 64bit unsigned integers. `BIG_SUM` allocates memory and
  stores the value in the newly allocated area. Finally, pushes the address of
  the result back to the stack.

### Primitive routines

- `print_big(x)`: 254

  `print_big` receives one parameter from the stack and prints it on
  stdout. It should treat `x` as reference to an unsigned big
  integer. `print_big` returns `0`.


### Machine memory

```
[ ........ program code ...... program stack ......heap ...] // memory
             ^                      ^      ^
             IP                     FP     SP
```

Memory is the same as `Machine #7`, with the addition of a `heap`. All results
of `BIG_SUM` should be in the `heap`, satisfying the following:

- Each stack frame / routine call keeps track of their own heap.
- All heap addresses must fit `operand` size to be able to be referenced by
  the stack operations.
- At the end of execution of a routine, (e.g. at `RET`), the heap of the
  respective routine should be deallocated.

To implement this, keep the heap address of each routine in the stack frame.
The activation record format should be: `[... prog_data, args, FP, ret_addr,
heap_addr, local_vars, prog_data ...]`, where `heap_addr` points to the heap
of that particular subroutine.

A simple way is to `[m|re]alloc`ing on every `BIG_SUM` and `free` the heap
region pointed by `heap_addr` at the end of the routine's execution.


### Programs

A program for `Machine #8` has similar format of programs for `Machine #7`
with a new `data_len` field and `data` section after `reloc_table`:

#### header

A header is divided in:

```
[ main_addr                : word-size bits]  //main routine address
[ reloc_table_size         : word-size bits]  //begin reloc_table
[ reloc_addr#1             : word-size bits]
[ reloc_addr#2             : word-size bits]
[ ...                                      ]
[ reloc_addr#N             : word-size bits] //end reloc_table
[ data_len                 : word-size bits] //size of data section
[ ....                                     ] //data section
```

The `main_addr` and `reloc_table` works as in `Machine #7`. However, not only,
all `CALL` instruction operands should have an entry in `reloc_table` but also
all `PUSH_DATA` operands should have a respective entry in this table.

Finally, the section `data` has `data_len` bytes of length.


#### body

The same as `Machine #7`

### Loading and linking programs

The same as `Machine #7`.

### Execution

The same as `Machine #7`.

### Usage

Same as `Machine #7`.

### Bonus

Create an assembler `a8`, in python, to build programs for `m8`. The assembler
should offer a convenient syntax for referencing data that should be in the
`data` section.


Example of source code, where brackets denote reference to values in `data`
section:

```
routine 0 { // print_big(4611686018427381104+4510686014400030899)
  push_data [4611686018427381104]
  push_data [4510686014400030899]
  big_sum
  push 1
  pcall 254
  ret
}
```

for every `PUSH_DATA` operation:

- `PUSH_DATA`s operands should be stored in `data` section and it's operand
  should become the address of the data within `data` section.
- an entry in the relocation table should be added for the `PUSH_DATA` operand.

Assembled, the source code above should generate the following object file:

```
//header
0x0:  ?                       //main_addr
0x1:  2                       //reloc_table_size
0x2:  ?                       //entry#1
0x3:  ?                       //entry#2
0x4:  16                      //data_len: 16 bytes
0x5:  4611686018427381104     //data#1
0xD:  4510686014400030899     //data#2
//body
0x15: 0xC 0x5    //push_data [4611686018427381104] -- begin subroutine 0
0x17: 0xC 0xD    //push_data [4510686014400030899]
0x19: 0xD 0      //big_sum
0x23: 1 1        //push 1
0x25: 5 254      //pcall 254
0x27: 7 0        //ret
```

This program should print `9122372032827412003` and exit.
