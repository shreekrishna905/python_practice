from functools import wraps


def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print('Result is too big ({0}) greater than ({1})'.format(result, threshold))
            return result
        return wrapper
    return decorator


@max_result(500)
def cube(n):
    return n ** 3


if __name__ == "__main__":
    print(cube(7))