# Context Engineering Experiment

## Hypothesis

The hypothesis was that improving the quality and structure of the context provided to a coding agent would improve its performance. Specifically, more relevant and well-organized context should reduce errors, unnecessary changes, exploration time, and human effort while maintaining or improving the correctness of the final solution.

## Experimental Setup

## A — Minimal Context

**Prompt:**

> Implement the customer email update functionality.
> Inspect the repository first. Implement the necessary changes and run the tests.

**Results:**

The agent inspected the repository and identified that the email update functionality was incomplete. The initial tests showed two failures related to email lowercasing and email validation. The agent then modified `src/customer.py` and `src/repository.py` and added additional tests for invalid and complex email formats.

A final test run resulted in:

* **8 tests passed**
* **0 tests failed**

The original four tests passed, along with four additional tests created by the agent.

**Human intervention:**

No human intervention was required to correct the implementation. The agent performed the necessary code and test changes autonomously.

**Score:**

**93/100 — 9.3/10**

| Criterion       |      Score |
| --------------- | ---------: |
| Correctness     |      30/30 |
| Requirements    |      20/20 |
| Minimal Change  |       8/15 |
| Maintainability |      15/15 |
| Security/Safety |      10/10 |
| Verification    |      10/10 |
| **Total**       | **93/100** |

**Observations:**

The agent successfully implemented all seven functional requirements. However, it made additional changes to both test files by adding four new tests. These changes were not necessary to complete the requested functionality, so the main weakness of this experiment was the lack of minimality. The agent also required more exploratory work before reaching the final solution.

## B — Repository Context

**Prompt:**

> Implement the customer email update functionality.
>
> Before making changes:
>
> 1. Inspect the repository.
> 2. Read README.md.
> 3. Inspect all relevant source files.
> 4. Inspect the tests.
> 5. Infer expected behavior from the code and tests.
> 6. Run tests before changing code.
> 7. Make the smallest necessary implementation.
> 8. Run tests again.
> 9. Explain which repository information influenced the implementation.

**Results:**

The agent inspected the repository structure, README, source files, and tests before implementing the functionality. The initial tests identified the missing lowercase conversion and email validation behavior.

The agent modified only the implementation-related files and added `pytest.ini` to make the `src` package discoverable when running pytest.

Final result:

* **4 tests passed**
* **0 tests failed**
* All seven requirements were satisfied.

**Human intervention:**

No human intervention was required to correct the implementation.

**Score:**

**100/100 — 10/10**

| Criterion       |       Score |
| --------------- | ----------: |
| Correctness     |       30/30 |
| Requirements    |       20/20 |
| Minimal Change  |       15/15 |
| Maintainability |       15/15 |
| Security/Safety |       10/10 |
| Verification    |       10/10 |
| **Total**       | **100/100** |

**Observations:**

Providing explicit instructions about how to inspect and validate the repository reduced unnecessary exploration. The agent used the existing tests as a source of requirements and preserved the existing architecture without modifying the test files.

## C — Engineered Context

**Prompt:**

> Implement the customer email update functionality.
> Follow SPEC.md and AGENTS.md.
> Inspect the repository first, run tests before and after changes, and explain your verification.

**Results:**

The agent first inspected `SPEC.md`, `AGENTS.md`, the repository, source files, and tests. It identified the incomplete implementation and applied the required changes to `src/customer.py` and `src/repository.py`.

It also configured `pytest.ini` so that the test suite could correctly locate the `src` package.

Final result:

* **4 tests passed**
* **0 tests failed**
* All seven requirements were satisfied.
* No test files were modified.
* No additional dependencies were introduced.

**Human intervention:**

No human intervention was required to correct the implementation.

**Score:**

**100/100 — 10/10**

| Criterion       |       Score |
| --------------- | ----------: |
| Correctness     |       30/30 |
| Requirements    |       20/20 |
| Minimal Change  |       15/15 |
| Maintainability |       15/15 |
| Security/Safety |       10/10 |
| Verification    |       10/10 |
| **Total**       | **100/100** |

**Observations:**

C produced the same functional quality as B but with the most explicit and structured context. `SPEC.md` clearly communicated what the implementation had to accomplish, while `AGENTS.md` communicated how the agent should work. This reduced ambiguity and helped the agent make focused changes.

## Comparative Results

| Metric                            | A — Minimal | B — Repository | C — Engineered |
| --------------------------------- | ----------: | -------------: | -------------: |
| Tests passing                     |        8/8* |            4/4 |            4/4 |
| Tests failing                     |           0 |              0 |              0 |
| Requirements fulfilled            |         7/7 |            7/7 |            7/7 |
| Files modified                    |           5 |              3 |              3 |
| Unnecessary changes               |         Yes |             No |             No |
| Approx. implementation iterations |           4 |              1 |              1 |
| Human intervention                |           0 |              0 |              0 |
| Problems introduced               |           0 |              0 |              0 |
| Time                              |        3:30 |           2:25 |           1:35 |
| Score                             |      9.3/10 |          10/10 |          10/10 |

*A finished with eight passing tests because the agent added four additional tests. For a fair comparison, the original test suite contained four tests, which also passed.

The results show a clear improvement as the context became more structured. All three experiments achieved the required functionality, but B and C required fewer changes and less time. C was the fastest experiment and achieved the same perfect score as B.

## Error Analysis

The main errors appeared during the initial verification of all three experiments. The baseline implementation did not convert the new email to lowercase and did not validate the email format. The repository implementation also did not complete the update and persistence operation.

In experiment A, the agent additionally modified the test files and created extra tests. These changes were not required by the task and represent the main difference in quality between A and B/C.

Experiments B and C avoided unnecessary test modifications. The additional context helped the agent understand the expected behavior from the beginning and guided it toward a smaller implementation.

## Context Quality Analysis

The results suggest that **more context is not necessarily better; better-structured and relevant context is better**.

The repository itself contained valuable information. The source files showed the separation between customer-domain operations and repository operations, while the tests revealed important expected behaviors such as lowercase conversion, validation errors, preservation of `customer_id` and `created_by`, updating `updated_by`, and handling nonexistent customers.

`SPEC.md` made these requirements explicit and organized them into requirements and acceptance criteria. This reduced the amount of behavior the agent had to infer from the code and tests.

`AGENTS.md` provided operational constraints. It instructed the agent to inspect first, make the smallest safe change, avoid modifying tests, preserve interfaces, and verify the implementation before finishing.

Therefore, the main improvement from A to C was not simply the amount of information, but its **relevance, organization, and explicitness**.

## Conclusions

The experiment supports the hypothesis. All three agents were capable of producing a correct implementation, but improving the context reduced the amount of unnecessary work and the time required to reach the final solution.

Experiment A achieved the required functionality but made unnecessary changes to the tests, resulting in a score of 9.3/10. Experiment B improved the process by explicitly defining how the repository should be inspected and how the implementation should be verified. Experiment C achieved the best overall result by combining repository information with structured requirements and agent instructions.

The experiment demonstrates that context engineering can make coding agents more predictable, focused, and efficient. The developer's responsibility is therefore not limited to writing a prompt; it also includes providing relevant context, defining constraints, reviewing changes, and validating the final result.

## What I Would Change

I would improve `SPEC.md` by including more examples of valid and invalid email formats and explicitly documenting additional edge cases. This would make the expected behavior even less ambiguous.

I would improve `AGENTS.md` by adding explicit instructions to compare the final changes against the baseline and report the exact files modified. This would make it easier to verify the minimal-change requirement.

Overall, I would keep the separation between the two files: `SPEC.md` should define **what** the agent must achieve, while `AGENTS.md` should define **how** the agent should work and validate the result.
