# 0x00-pagination

## Task 0

The function does the following:

1. It takes two integer arguments: `page` and `page_size`.
2. It calculates the `start_index` by multiplying `(page - 1)` by `page_size`. We subtract 1 from `page` because the function uses 1-indexing for pages, but we need 0-indexing for list indices.
3. It calculates the `end_index` by adding `page_size` to the `start_index`.
4. It returns a tuple containing `start_index` and `end_index`.

The function uses type hints to indicate that it takes two integers as input and returns a tuple.

## Task 1

Let's break down the `get_page` method:

1. We use `assert` statements to verify that both `page` and `page_size` are integers greater than 0. If these conditions are not met, an `AssertionError` will be raised.

2. We get the dataset using the `dataset()` method.

3. We use a try-except block to handle cases where the requested page is out of range:
   - We call `index_range(page, page_size)` to get the start and end indices.
   - We return the slice of the dataset from start to end.
   - If an `IndexError` occurs (which would happen if the start index is beyond the end of the dataset), we catch it and return an empty list.

## Task 2

Let's break down the `get_hyper` method:

1. We reuse the `get_page` method to retrieve the data for the current page.

2. We calculate the total number of rows in the dataset using `len(self.dataset())`.

3. We calculate the total number of pages using `math.ceil(total_rows / page_size)`. This ensures that we round up to include any partial last page.

4. We create and return a dictionary with the required key-value pairs:
   - `page_size`: the length of the returned dataset page
   - `page`: the current page number
   - `data`: the dataset page (from `get_page`)
   - `next_page`: the number of the next page, or `None` if this is the last page
   - `prev_page`: the number of the previous page, or `None` if this is the first page
   - `total_pages`: the total number of pages in the dataset
