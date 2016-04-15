# Machine #4

**Goal**: Extend [Machine 3](exercise_03.md) with user-defined subroutines.

### Instruction format

(The same as and `Machine #3`)

- Word size: 16 bits.
- operation section: 8 bits
- operand section: 8 bits

`[ operation 8bits | operand 8bits ]`

All instructions are 16 bits long, even if the operation does not have arguments (in that case, operand section should be ignored).

#### Instruction set

This machine introduces `CALL` and `RET` opcodes


- `PUSH <ARG>`: 0x1
- `POP`:  0x2
- `SUM`:  0x3
- `SUMX`: 0x4
- `PCALL <ID>`: 0x5
- `CALL <ID>`: 0x6

  `CALL <ID>` transfers the execution to the user-defined subroutine identified by `ID`. When the subroutine finishes execution, it's resulting value should be at the top of the stack.

- `RET`: 0x7

  `RET` uses the top value of the stack as the `result` of the subroutine. It clears the stack frame for the current subroutine and at the end, pushes `result` so the caller can obtain it at the top of the stack.

### Machine memory

```
[ ........ program code ...... program stack ....] // memory
             ^                      ^      ^
             IP                     FP     SP
```


This machine is allowed to have an extra *register*: `FP` (*frame
pointer*). This register purpose is to identify the `activation records` of
the subroutines. **Note**: Subroutines should not use the C-stack!

### Execution

The activation record format should be: `[... local_data, FP, ret_addr, local_data ...]`, where:

- `FP` is the current value stored in `FP`
- `ret_addr` is a pointer to the next instruction of the call site.
- `local_data` is all local data  a subroutine pushes to operate on.

For example, consider the following code containing a call to some subroutine `X` (as in `X()`):

```
0xA: PUSH 10
0xB: PUSH 20
0xC: SUM
0xD: CALL X
0xE: PUSH 40
```

Upon executing `CALL X`:

- The value in `FP` should be pushed on the stack.
- `FP` should be set to `SP` of the call site
- the address of the next instruction (`0xE`) should be pushed on the stack.

Then, the stack contents should be:

```
0x03: ...                 //local_data
0x04: 10                  //local_data
0x05: 20                  //local_data
0x06: <previous FP value> //FP
0x07: 0xE                 //ret_addr
```

And the register contents should be:

```
FP = 0x06 //previous FP
SP = 0x07
```

In this way, `FP` always points to the previous `FP` (recursively) and `FP+1` points to the next instruction of the call site.

When `RET` is executed, `FP` should be used to:

- reset  `IP` to the address of the next instruction to be executed using `FP` (ie. `0xE`)
- clear the stack from local data pushed during `X` execution, reseting `SP` to it's previous value (which is `FP-1`).
- reset the previous value of `FP`.

### Programs

A program for `Machine #4` has two sections: a `header`, and a `body`. The `header` is a table of routines, and the `body`  contains all code of all subroutines defined:

```
[ header ]
[ body ]
```

#### header

The format of the header is:

```
[ num_entries: 16 bits]
[ entry#1 id: 16 bits | entry#1 ptr: 16 bits]
[ entry#2 id: 16 bits | entry#2 ptr: 16 bits]
...
[ entry#<N> id: 16 bits | entry#<N> ptr: 16 bits]
```
where `<N> == num_entries`.

The `entry id` is the value that corresponds to the `id` of a user defined subroutine. The `entry ptr` is a pointer to the first instruction of that routine in the `body` section, with offset'd by `len(header)`.

So, for example, if `num_entries` is 3, and considering an `entry` has length 32 (16 for `id` and 16 fo `ptr`), then the remaining header length is `3*32`, which is 96 bits.



#### body

The `body` of a program is just a concatenation of user-defined subroutine bodies -- a subroutine body is just a string of instructions. The `header` should contain pointers to the beginning of each routine in this section.

All subroutine bodies should end with `RET <VAL>` instruction.

### Usage

Same as `Machine #3`.

### Loading programs

Programs are loaded by reading the `header` and looking for the entry numbered `0`. That's the `main` routine to be executed. The VM should fail if no entry `id` 0 is found. Upon finding such entry, the VM should start executing the code pointed by the `ptr` of that routine.

### Bonus

Create an assembler `a4`, in python, to build programs for `m4`. The assembler should be able to create binary programs given a source code. The source code is just a collection of subroutines whose instructions are per line. Example of source code:

```
routine 7 { //  1+2
  push 1
  push 2
  sum
  ret
}

routine 0 { // print(7()+10)
  push 10
  call 7
  sum
  push 1
  pcall 255
  ret
}
```

Alternate syntax are welcome, if they could make parsing easier (these are not exercises on compilation :)).

Assembled, the source code above should generate the following object file:

```
//header
2     //num_entries
7 0   //entry id: 7, entry ptr: 0
0 8   //entry_id: 0, entry ptr: 8
//body
1 1   //push 1  -- begin subroutine 7
1 2   //push 2
3 0   //sum
7 0   //ret
1 10  //push 10 -- begin subroutine 0
6 7   //call 7
3 0   //sum
1 1   //push 1
5 255 //pcall 255
7 0   //ret
```

This program should print `13` and exit.
