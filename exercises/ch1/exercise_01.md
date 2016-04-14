# Machine #1

**Goal**: very very basic stack interpreter.

### Instructions

Opcodes: `PUSH`, `POP`, `SUM`, `SUMX`

### Basic API:

```python
>>> m1 = Machine1()
>>> m1.dump_stack()
[]
```

### `PUSH <ARG>`

```python
>>> m1.evaluate(['PUSH', 10])
>>> m1.dump_stack()
[10]
```

### `POP`

```python
>>> m1.evaluate(['PUSH', 10, 'POP'])
>>> m1.dump_stack()
[]
```
### `SUM`

pops and sums the 2 topmost values on the stack and pushes the result.

```python
>>> m1.evaluate(['PUSH', 11, 'PUSH', 22, 'PUSH', 33, 'SUM'])
>>> m1.dump_stack()
[11, 55]
```

### `SUMX`

let `len` be the topmost value popped from the stack: `SUMX` pops and sums the top `len` values on the stack and pushes the result.

```python
>>> m1.evaluate(['PUSH', 4, 'PUSH', 5, 'PUSH', 6, 'PUSH', 3, 'SUMX'])
>>> m1.dump_stack()
[15]
```
