# Choosing Boxes

## Constrained Quadratic Model (Hybrid Solver)
You're given three boxes with values 17, 21, and 19.

Write a CQM and an Ocean program that returns the pair of boxes with the
smallest sum.  A starter file has been provided for you in
``ex1_cqm.py``.

### Instructions

To write your program, please complete the following in `ex1_cqm.py`:

- Build your CQM in the ``get_cqm`` function.
- Complete the main function (bottom of the file) by defining a sampler,
  running your problem on that sampler, and looking at the results.  "Looking
at the results" may be as simple as printing out the sampleset object - it's up
to you!

## Binary Quadratic Model (QPU)

Write a CQM and an Ocean program that returns the pair of boxes with the
smallest sum.  A starter file has been provided for you in
``ex2_bqm.py``.

**Remember:**

You will need to choose a value for your Lagrange parameter and number of QPU
reads.  The autograder will test if your Lagrange parameter is large enough
that the desired solution (boxes 17 and 19) has the smallest value.

## Instructions

To write your program, please complete the following in `ex2_bqm.py`:

- Build your BQM in the ``get_bqm`` function, and set the Lagrange parameter.
- Find a good value ``numruns`` in the ``run_on_qpu`` function
- Complete the main function (bottom of the file) by defining a sampler,
  running your problem on that sampler, and looking at the results.  "Looking
at the results" may be as simple as printing out the sampleset object - it's up
to you!

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.
