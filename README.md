# Thiago's VM crash course


## Goal

This course should guide lost souls into constructing a stack based virtual
machine and all the pains that go into building one, following the smalltalk
and lisp tradition. Expect old and modern techniques to make appearences.

## Before start

- This is a very terse course (aimed at professional programmers)
- Each exercise was designed to be completed in `< 1 hour`.
- The first exercises of each chapter require some infra-structures so may
  take a little longer.
- Your medium must to be a system programming language like C -- there's no
  point in trying to learn how things work under the hood if one is always
  over the hood (the exception is the warm up exercise #1 where a highlevel
  language is permitted to be used).
- Compiler writing skills will make your life easier, but these texts won't
  talk about parsing nor about code generation.


## Table of Contents

### Chapter 1
*Level: :suspect:, Time: :clock1:*

- [Exercise #1: Basic python stack machine](exercises/ch1/exercise_01.md)
- [Exercise #2: Basic C stack machine](exercises/chapter_02.md)
- [Exercise #3: VM with primitive routines](exercises/chapter_03.md)
- [Exercise #4: VM with user-defined routines](exercises/chapter_04.md)
- [Exercise #5: VM with parameterized user-defined routines](exercises/chapter_05.md)

### Chapter 2
*Level: :hurtrealbad:, Time: :clock2:*

- Exercise #4: VM with user-defined routines
- Exercise #5: user defined routines with parameters
- Exercise #X: lower-level-style calls
- Exercise #X: local variables
- Exercise #X: strings
- Exercise #X: conditionals and loops
- Exercise #X: first class functions / closures
- Exercise #X: classes
- Exercise #X: exceptions


---

Other topics:
 - var args
 - modules/importing
 - bindings
 - GC'ing
 - C-stack vs. stackless
 - Higher level conditionals/loops (smalltalk style)
 - `call/cc`
 - co-routines
 - JS-style objects
 - piumarta-style objects
 - JIT compilation
 - Exposing interactive debugging facilities (bonus: reifying the stack)
 - multi-methods
 - Mixins
