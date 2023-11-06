[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/vgoliber/cqm-bqm-exercises/blob/live-workshop?quickstart=1)
  
# Choosing Boxes

We're given three boxes with values 17, 21, and 19. We want to choose the pair of boxes with the smallest sum. In the next few exercises, we will solve this with different quadratic models and D-Wave solvers.

## Building a Model

In this first exercise, we will build a quadratic model to represent the problem.

### Instructions

To build your model, complete the following steps.

- Write (in words, not math) the objective and constraint for this problem
- Define binary variables and translate your objective and constraint into mathematical expressions

## Constrained Quadratic Model (Hybrid Solver)

Write a CQM and an Ocean program that returns the pair of boxes with the
smallest sum.  A starter file has been provided for you in
``ex1_cqm.py``.

### Instructions

To write your program, please complete the following in `ex1_cqm.py`:

- Build your CQM in the ``get_cqm`` function
- Complete the main function (bottom of the file) by defining a sampler,
  running your problem on that sampler, and looking at the results.  "Looking
at the results" may be as simple as printing out the sampleset object - it's up
to you!

## Binary Quadratic Model (QPU)

Write a BQM and an Ocean program that returns the pair of boxes with the
smallest sum.  A starter file has been provided for you in
``ex2_bqm.py``.

**Remember:**

You will need to choose a value for your Lagrange parameter and number of QPU
reads.  The excel file included in this repository can help you to select a large enough parameter.

### Instructions

To write your program, please complete the following in `ex2_bqm.py`:

- Build your BQM in the ``get_bqm`` function, and set the Lagrange parameter
- Find a good value for ``numruns`` in the ``run_on_qpu`` function
- Complete the main function (bottom of the file) by defining a sampler,
  running your problem on that sampler, and looking at the results.  
  
If you have extra time, try calling the problem inspector to see how your problem is embedded onto the QPU.

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.
