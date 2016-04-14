# Machine #3

**Goal**: Extend [Machine 2](https://github.com/thiago-silva/vm-crash-course/blob/master/exercises/ch1/exercise_02.md) with a primitive call instructions.

### Instruction format

(The same as `Machine #2`)

- Word size: 16 bits.
- operation section: 8 bits
- operand section: 8 bits

`[ operation 8bits | operand 8bits ]`

All instructions are 16 bits long, even if the operation does not have arguments (in that case, operand section should be ignored).

#### Instruction set

This machine introduces `PCALL` opcode


- `PUSH <ARG>`: 0x1
- `POP`:  0x2
- `SUM`:  0x3
- `SUMX`: 0x4
- `PCALL <ID>`: 0x5

`PCALL <ID>` takes the topmost value on the stack as the `argc` and the remaining `argc` values on the stack as arguments to subroutine `id`. When the routine finishes execution, the stack frame should be substituted by its resulting value at the top of the stack.

### Machine memory


```
[ ........ program code ...... program stack ....] // memory
             ^                             ^
             IP                            SP
```


Same as `Machine #2`.

### Programs

A program for `Machine #3` is the same as for `Machine #2`, but extended with `PCALL` instruction

#### Execution

Same as `Machine #2`.

### Primitive routines

- `print(x)`: 255

  `print` receives one parameter from the stack and prints it on stdout. It returns `0`.

### Example

Given the stack `[3, 1]`, the operation `PCALL 255` interprets `1` to be `argc`, and the remaining `argc` (i.e. 1) value(s) on the stack -- `3` -- to be the argument to subroutine `255`. At the end, the stack should be `[0]` -- `0` being the result of the `print` operation.

### Usage

Same as `Machine #2`

