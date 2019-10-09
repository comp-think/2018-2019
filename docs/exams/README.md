# Written examinations (with keys)

In this page it is possible to find the link to the various written examination of the course Computational Thinking and Programming, academic year 2018/2019.

## 20 September 2019 written examination

**Text of the exam:** [PDF](https://comp-think.github.io/2018-2019/exams/written-examination-2019-09-20.pdf)

**Solutions:**
* Section 1 (theory):
  1. recursive-step
  
     leaf-lose
     
  2. ```
     def fib_dp(n, d=dict()):
        if n not in d:
           if n == 0 or n == 1:
              d[n] = n
           else:
              d[n] = fib_dp(n-1, d) + fib_dp(n-2, d)

        return d[n]
     ```
     
  3. Function defined as follows: 
     ```
     def f(s, n):
         return len(s) % n == 0
     ```
  4. These characteristics are that, at a certain step, we can choose the best candidate for improving the set of candidates bringing to a solution (*greedy choice*), and that the optimal solution to a computational problem can be built by considering the optimal solutions to its subproblems (*optimal substructure*).

* Section 2 (understanding): [Python script](https://comp-think.github.io/2018-2019/python/rs_written_examination_2019-09-20_ex2.py) to calculate the output of `rs(my_gn, my_fn, my_mn)` - run with `python rs_written_examination_2019-09-20_ex2.py` and follow the instructions.

* Section 3 (development): [implementation](https://comp-think.github.io/2018-2019/python/multiple_replace_written_examination_2019-09-20_ex3.py) of the function `multiple_replace`.

## 15 July 2019 written examination

**Text of the exam:** [PDF](https://comp-think.github.io/2018-2019/exams/written-examination-2019-07-15.pdf)

**Solutions:**
* Section 1 (theory):
  1. machine language
  
     high-level programming languages
  
     low-level programming languages
     
  2. ```
     def line_wrap(text, line_width):
        result = []
        space_left = line_width
        line = []

        for word in text.split(" "):
            word_len = len(word)
            if word_len + 1 > space_left:
                result.append(" ".join(line))
                line = [word]
                space_left = line_width - word_len
            else:
                line.append(word)
                space_left = space_left - word_len + 1

        result.append(" ".join(line))
        return "\n".join(result)
     ```
     
  3. Function defined as follows: 
     ```
     def f(fn, i1, i2):
         return fn(i1) == i2
     ```
  4. The main difference between the two approaches is that *dynamic programming*, in addition to what done by *divide and conquer*, stores the solutions of the subproblems already addressed for reusing them if they reoccur again. On the one hand, this technique allows one to save a huge amount of computation time if similar subproblems happen more than once. On the other hand, one needs additional memory space for storing the solutions to subproblems already addressed.

* Section 2 (understanding): [Python script](https://comp-think.github.io/2018-2019/python/char_n_written_examination_2019-07-15_ex2.py) to calculate the output of `char_n(my_gn, my_fn, my_mn)` - run with `python char_n_written_examination_2019-07-15_ex2.py` and follow the instructions.

* Section 3 (development): [implementation](https://comp-think.github.io/2018-2019/python/alive_in_next_step_written_examination_2019-07-15_ex3.py) of the function `alive_in_next_step`.

## 21 June 2019 written examination

**Text of the exam:** [PDF](https://comp-think.github.io/2018-2019/exams/written-examination-2019-06-21.pdf)

**Solutions:**
* Section 1 (theory):
  1. context-free grammars
  
     recursively enumerable grammars
  
     regular grammars
     
  2. 11
     
  3. Function defined as follows: 
     ```
     def f(n, l):
         result = 0
         for i in l:
             result += i
         return result == n"
     ```
  4. The data structures are *set* and *dictionary*. Both the data structures are countable collection of unordered entities. However, while an entity in the set is just an item and cannot be repeated, in a dictionary an entity is a key-value pair, where the key is non-repeatable in the dictionary, while the values are.  

* Section 2 (understanding): [Python script](https://comp-think.github.io/2018-2019/python/c_written_examination_2019-06-21_ex2.py) to calculate the output of `c(my_fn, my_mat)` - run with `python c_written_examination_2019-06-21_ex2.py` and follow the instructions.

* Section 3 (development): [implementation](https://comp-think.github.io/2018-2019/python/delta_decoding_written_examination_2019-06-21_ex3.py) of the function `delta_decoding`.

## 15 May 2019 written examination

**Text of the exam:** [PDF](https://comp-think.github.io/2018-2019/exams/written-examination-2019-05-15.pdf)

**Solutions:**
* Section 1 (theory):
  1. First in first out (FIFO)
  
     Last in first out (LIFO)
     
  2. `d[n] = 0` -> `d[n] = n`
     
     `d[n-1] = fib_dp(n-1, d) + fib_dp(n-2, d)` -> `d[n] = fib_dp(n-1, d) + fib_dp(n-2, d)`
     
  3. Function defined as follows: 
     ```
     def f(s, n):
         return s[n] in "aeiou"
     ```
  4. regular grammars – form of production rules: ​`<non-terminal> ::= "terminal"` and `​<non-terminal> ::= "terminal" <non-terminal>`
     
     context-free grammars​ – form of production rules: ​`<non-terminal> ::= γ`
     
     context-sensitive grammars – form of production rules: ​`α <non-terminal> β ::= α γ β​`
     
     recursively enumerable grammars – form of production rules: `​α ::= β`

* Section 2 (understanding): [Python script](https://comp-think.github.io/2018-2019/python/m_written_examination_2019-05-15_ex2.py) to calculate the output of `m(my_gr, my_fn, my_mat)` - run with `python m_written_examination_2019-05-15_ex2.py` and follow the instructions.

* Section 3 (development): [implementation](https://comp-think.github.io/2018-2019/python/delta_encoding_written_examination_2019-05-15_ex3.py) of the function `delta_encoding`.

## 15 March 2019 written examination

**Text of the exam:** [PDF](https://comp-think.github.io/2018-2019/exams/written-examination-2019-03-15.pdf)

**Solutions:**
* Section 1 (theory):
  1. True or False
  
     not False and (True or False)
     
     True and not (True and False)
     
     not (False and not True) or False
     
  2. The return value is `"bro"`.
  3. Function defined as follows: 
     ```
     def f(s1, s2):
         if len(s1) > len(s2):
             return -1
         elif len(s1) < len(s2):
             return 1
         else:
             return 0
     ```
  4. The problem of the seven bridges of the city of Königsberg can be stated as follows: is it possible to walk around the city and to cross each of the bridges once and only once? Resolution: each land in Königsberg, excepting the starting land and the final land, should have an even number of bridges in order to be sure one can enter and then go out from it. However, all the lands have an odd number of bridges, thus it is not possible to solve the problem satisfactorily.

* Section 2 (understanding): [Python script](https://comp-think.github.io/2018-2019/python/f_written_examination_2019-03-15_ex2.py) to calculate the output of `f(my_fn, my_mn)` - run with `python f_written_examination_2019-03-15_ex2.py` and follow the instructions.

* Section 3 (development): [implementation](https://comp-think.github.io/2018-2019/python/rabin_karp_written_examination_2019-03-15_ex3.py) of the function `rabin_karp`.

## 4 February 2019 written examination

**Text of the exam:** [PDF](https://comp-think.github.io/2018-2019/exams/written-examination-2019-02-04.pdf)

**Solutions:**
* Section 1 (theory):
  1. flowline widget
  
     decision widget
     
     process widget
     
  2. The line `mid = partition(input_list, 0, input_list_len, 0)` must be replaced with `input_list_len // 2`.
  3. Function defined as follows: 
     ```
     def f(i1, i2):
         return (i1 % 2) + (i2 % 2) == 0
     ```
  4. A recursive function must have at least one **basic case**, which describe the terminating scenario that does not use any recursion to product the answer to a specific (sub-)problem, and the **recursion step**, which is where the same algorithm is executed again with a different (and, usually, reduced) input.

* Section 2 (understanding): [Python script](https://comp-think.github.io/2018-2019/python/r_written_examination_2019-02-04_ex2.py) to calculate the output of `r(my_gn, my_fn)` - run with `python r_written_examination_2019-02-04_ex2.py` and follow the instructions.

* Section 3 (development): [implementation](https://comp-think.github.io/2018-2019/python/bigrams_jaccard_written_examination_2019-02-04_ex3.py) of the function `bigrams_jaccard`.


## 25 January 2019 written examination

**Text of the exam:** [PDF](https://comp-think.github.io/2018-2019/exams/written-examination-2019-01-25.pdf)

**Solutions:**
* Section 1 (theory):
  1. an infinite memory tape
     
     an head
     
     a way to record the current state of the machine, an initial state and zero or more final states
     
     a table of instructions
  2. 8
  3. Function defined as follows: 
     ```
     def f(c, k):
         return c * k
     ```
  4. [leaf-win] if current node is a leaf and it is a solution then return it, otherwise; 
  
     [leaf-lose] if current node is a leaf but it is not a solution, then return no solution back the parent node, otherwise; 
     
     [recursive-step] apply recursively the whole approach for each child of the current node, until one of these recursive executions returns a solution - if no solution, go back the parent node of the current one.

* Section 2 (understanding): [Python script](https://comp-think.github.io/2018-2019/python/s_prepare_written_examination_2019-01-25_ex2.py) to calculate the output of `s(prepare(my_string_id))` - run with `python s_prepare_written_examination_2019-01-25_ex2.py` and follow the instructions.

* Section 3 (development): [implementation](https://comp-think.github.io/2018-2019/python/k_hash_written_examination_2019-01-25_ex3.py) of the function `k_hash`.
