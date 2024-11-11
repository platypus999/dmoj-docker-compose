from dmoj.result import CheckerResult

def check(process_output, judge_output, judge_input, point_value, **kwargs):
    # convert from bytes to texts
    process_output = process_output.decode("ascii")
    judge_output = judge_output.decode("ascii")
    judge_input = judge_input.decode("ascii")

    source_code = kwargs["submission_source"]

    source_code = source_code.decode("utf-8")

    if "+" in source_code:
        return CheckerResult(False, 0, "You can't use + operator")

    if len(source_code) >= 100:
        return CheckerResult(False, 0, "Source code is too long")

    # read data as normal
    input_lines = [line.strip() for line in judge_input.split('\n') if line.strip()]
    output_lines = [line.strip() for line in process_output.split('\n') if line.strip()]
    N = int(input_lines[0])
    if len(output_lines) != N:
        return CheckerResult(False, 0, f"Expected {N} lines of output, got {len(output_lines)}")
    for i in range(N):
        a, b = map(int, input_lines[i + 1].split())
        if a + b != int(output_lines[i]):
            return CheckerResult(False, 0, f"{a} + {b} != {output_lines[i]}")
    return CheckerResult(True, 100 - len(source_code), "Ok answer is correct")