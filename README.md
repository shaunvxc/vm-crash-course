# Thiago's VM crash course


## About

This course should help ~~lost souls~~ programmers to construct virtual
machines and understand many of the issues that go with designing one. The
main goal is to dismistify how VMs and interpreters work while also showing
the power of being able to create them.

The target audience for this material are the curious programmers who wonder
about what lies beneath the hood of the interpreters they use
everyday. Moreover, mong these there might be a hacker who plans to actually
build his own language and system one day.

The themes explored here are those of [single] stack based virtual
machines. There won't be journeys to multi-stack machines nor register based
ones. However, expect old and modern techniques to make appearences.

## Before start

- This is a very terse course entirely based on exercises.

- Each exercise was designed to be an increment over the predecessor and they
  should be completed in `< 1 hour`.

- The exercises in itallics require more effort, so may take a little longer.

- Your medium must be a system programming language like C or anything that
  manipulates raw memory with pointers. There's no point in trying to learn
  how things work under the hood if one is always over the hood; the exception
  is the warm up exercise #1 where a highlevel language is permitted to be
  used.

- Compiler writing skills might come in handy, but for most part, only basic
  understanding of text manipulation is necessary.


## Discussing solutions

If you want to present your solutions and/or discuss them, do the following:

1. Fork this repository
2. Create a branch following the pattern chX/YY (e.g., ch1/01, ch1/02)
3. Push to that branch
4. Create a pull request to my repository with the title "chX/YY by [username]" (e.g., ch1/01 by hltbra)
5. Wait for comments.

If you are suggestion a solution, feel free to leave the pull request opened
so other people can learn too.

## Table of Contents

### Chapter 1
*Level: :suspect:, Time: :clock6:*

- [Exercise #1: Basic stack machine in python](exercises/ch1/exercise_01.md)
- [Exercise #2: Basic stack machine in C](exercises/ch1/exercise_02.md)
- [Exercise #3: VM with primitive routines](exercises/ch1/exercise_03.md)
- *[Exercise #4: VM with user-defined routines](exercises/ch1/exercise_04.md)*
- [Exercise #5: VM with parameterized user-defined routines](exercises/ch1/exercise_05.md)


### Chapter 2
*Level: :hurtrealbad:, Time: :clock1:*

WIP

### Chapter 3
*Level: :rage2:, Time: :clock1:*

WIP

### Chapter 4
*Level: :goberserk:, Time: :clock1:*

WIP

### Chapter 5
*Level: :finnadie:, Time: :clock1:*

WIP
