# Machine #2

**Goal**: Port [Machine #1](https://github.com/thiago-silva/vm-crash-course/blob/master/exercises/ch1/exercise_01.md) to C.

#### References:

- Quick
  - [Wikipedia's stack verbete](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)#Basic_architecture_of_a_stack)
  - [U of Maryland's CS class notes](https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Mips/stack.html)
- Non quick
  - [Programming Language Pragmatics](http://www.amazon.com/Programming-Language-Pragmatics-Second-Edition/dp/0126339511?ie=UTF8&psc=1&redirect=true&ref_=oh_aui_detailpage_o02_s01)
  - [Smalltalk-80 blue book](http://stephane.ducasse.free.fr/FreeBooks/BlueBook/Bluebook.pdf)

### Instruction format

- Word size: 16 bits.
- operation section: 8 bits
- operand section: 8 bits

`[ operation 8bits | operand 8bits ]`

All instructions are 16 bits long, even if the operation does not have arguments (in that case, operand section should be ignored).

#### Instruction set

- `PUSH <ARG>`: 0x1
- `POP`:  0x2
- `SUM`:  0x3
- `SUMX`: 0x4

The semantic of the operations above should conform with their specification given on the description for Machine #1.

Examples of instructions in bits:

 - `PUSH 10`: `00000001 00001010`
 - `SUMX`: `00000100 00000000`

#### Machine memory

```
[ ........ program code ...... program stack ....] // memory
             ^                             ^
             IP                            SP
```

The machine has a single memory -- RAM -- where both the program code and the
program data resides. On initializing, the VM should:

- Load the `program code` into memory
- Setup a `program stack` in memory

The machine has only two registers to localize itself in the memory:

- Instruction pointer (`IP`)

 This is a single variable that should point to a position in the `program
 code`, where the next instruction should be executed.

- Stack pointer (`SP`)

 This is a single variable that should point to the top of the `program stack`
 i.e. to the last value `pushed` to it.

### Programs

A program for `Machine #2` is a sequence of 16bit instructions stored in a file.

For example, the 3-instructions program `PUSH 1, PUSH 2, SUM` is encoded as `00000001 00000001 00000001 00000010 00000011 00000000`


#### Execution

- Instructions should be fetched using `IP`
- Whenever `IP` points to `0x0` it should exit -- this should be the last
  value in the program code.

### Usage

Basic command line usage:

```bash
$ ./m2 program.m2
[5,1,7]
$
```

...where `program.m2` is a binary file containing instructions for `m2` to execute -- you should write this file either manually, or with the aid of an assembler, see below. `m2` should execute all instructions and, at the end, pretty-print the stack and exit.


### Bonus

Create an assembler `a2`, in python, to build programs for machine `m2`. The assembler should be able to create binary programs given a source code -- one instruction per line. Example of source code:

```
push 1
push 2
sum
```
