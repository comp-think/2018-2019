# Written examinations (with keys)

In this page it is possible to find the link to the various written examination of the course Computational Thinking and Programming, academic year 2018/2019.

## 25 January 2019 written examination

**Text of the exam:** [PDF](https://comp-think.github.io/2018-2019/exams/written-examination-2019-01.pdf)

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