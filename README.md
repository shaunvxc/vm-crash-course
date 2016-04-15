# Thiago's VM crash course


## About

This course should help ~~lost souls~~ programmers into constructing virtual
machines and many of the issues that go with building one. The main goal is
to dismistify how VMs and interpreters work while also showing the power of
being able to create them.

The main audience for this is the curious professional programmer who wonders
about life beneath the hood of the interpreters he/she use everyday. Among
these may be the hacker who plans to actually build his own language and
system one day.

The themes explored here are those of [single] stack based virtual
machines. There won't be journeys to multi-stack machines nor register based
ones. However, expect old and modern techniques to make appearences.


## Before start

- This is a very terse course entirely based on exercises.

- Each exercise was designed to be an increment over the predecessor and they
  should be completed in `< 1 hour`.

- The first exercises of each chapter might require some infra-structures so
  may take a little longer.

- Your medium must be a system programming language like C or anything that
  manipulates raw memory with pointers (there's no point in trying to learn
  how things work under the hood if one is always over the hood; the exception
  is the warm up exercise #1 where a highlevel language is permitted to be
  used).

- Compiler writing skills might make your life easier, but these texts won't
  discuss anything about parsing nor about code generation.


## Table of Contents

### Chapter 1
*Level: :suspect:, Time: :clock1:*

- [Exercise #1: Basic stack machine in python](exercises/ch1/exercise_01.md)
- [Exercise #2: Basic stack machine in C](exercises/ch1/exercise_02.md)
- [Exercise #3: VM with primitive routines](exercises/ch1/exercise_03.md)
- [Exercise #4: VM with user-defined routines](exercises/ch1/exercise_04.md)
- [Exercise #5: VM with parameterized user-defined routines](exercises/ch1/exercise_05.md)
- [Exercise #6: VM with static calls](exercises/ch1/exercise_06.md)

### Chapter 2
*Level: :hurtrealbad:, Time: :clock2:*

WIP
