# Machine #6

**Goal**: Extend [Machine 5](exercise_05.md) to support local variables.

### Instruction format

(The same as `Machine #5`)

Let:

- Word size: `sizeof(void*)` bits
- operation: `sizeof(void*)/2` bits
- operand: `sizeof(void*)/2` bits

Instruction format: `[ operation | operand ]`

All instructions are `sizeof(void*)` bits long, even if the operation does not have arguments (in that case, operand should be ignored).

#### Instruction set

This machine introduces `INC_SP`, `PUSH_LOCAL` and `POP_LOCAL` opcodes:


- `PUSH <ARG>`: 0x1
- `POP`:  0x2
- `SUM`:  0x3
- `SUMX`: 0x4
- `PCALL <ID>`: 0x5
- `CALL <ID>`: 0x6
- `RET`: 0x7
- `PUSH_ARG <ARG>`: 0x8
- `INC_SP <ARG>`: 0x9

    sets `SP` to `SP+ARG`.

- `PUSH_LOCAl <ARG>`: 0xA

    this operation pushes the local variable indexed by `<ARG>` to the top of
    the stack, where `<ARG>` refers to the `n-th` local variable of the
    current subroutine.

- `POP_LOCAl <ARG>`: 0xB

    this operation pops the stack into local variable indexed by `<ARG>`,
    where `<ARG>` refers to the `n-th` local variable of the current
    subroutine.

### Machine memory

```
[ ........ program code ...... program stack ....] // memory
             ^                      ^      ^
             IP                     FP     SP
```


Same as `Machine #5`

It's recommended to have the VM `program stack` operating uniformily over values of `word` size.

### Execution

The activation record format should be: `[... prog_data, args, FP, ret_addr, local_vars, prog_data ...]`, where:

- `args` are the values `PUSH`ed by the call site.
- `FP` is the current value stored in `FP`.
- `ret_addr` is a pointer to the next instruction of the call site.
- `prog_data` is all data a subroutine pushes to operate on.
- `local_vars` is the storage for local variables of the subroutine.

For example, consider the following code containing a call to some subroutine
`X` (as in `X(10, 20)`) which has one local variable:

```
0xA: PUSH 10
0xB: PUSH 20
0xC: CALL X
0xD: PUSH 40
```

Upon executing `CALL X`:

- The value in `FP` should be pushed on the stack.
- `FP` should be set to `SP` of the call site
- the address of the next instruction (`0xD`) should be pushed on the stack.
- Finally, `SP` makes room for one variable in `local_vars`

Then, the stack contents should be:

```
0x03: ...                  //local_data
0x04: 10                   //arg#1
0x05: 20                   //arg#2
0x06: <previous FP value>  //FP
0x07: 0xD                  //ret_addr
0x8:  ???                  //unitialized local variable
```

And the register contents should be:

```
FP = 0x06 //previous FP
SP = 0x07
```

In this way:

- `FP` always points to the previous `FP` (recursively)
- `FP-n` points to the `n-th` argument passed by the caller
- `FP+1` points to the next instruction of the call site
- `FP+1+m` points to the `m-th` local variable of the subroutine


### Programs

A program for `Machine #6` is the same as for `Machine #5`.

### Usage

Same as `Machine #5`.

### Loading programs

Same as `Machine #5`.

### Bonus

Create an assembler `a6`, in python, to build programs for `m6`. The assembler
should be able to create binary programs given a source code. The source code
is just a collection of subroutines whose instructions are per line. Example
of source code:

```
routine 7 {
  inc_sp 2     //two local variables
  push 30
  pop_local 1  //v1 = 30;
  push 70
  pop_local 2  //v2 = 70;
  push_local 1
  push_local 2
  sum          //return v1 + v2;
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

This program should print `110` and exit.
