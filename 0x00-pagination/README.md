# 0x00-pagination

## Task 0

The function does the following:

1. It takes two integer arguments: `page` and `page_size`.
2. It calculates the `start_index` by multiplying `(page - 1)` by `page_size`. We subtract 1 from `page` because the function uses 1-indexing for pages, but we need 0-indexing for list indices.
3. It calculates the `end_index` by adding `page_size` to the `start_index`.
4. It returns a tuple containing `start_index` and `end_index`.

The function uses type hints to indicate that it takes two integers as input and returns a tuple.

## Task 1
