def get_statistics(input_list):
    input_list.sort()
    mean = 0
    median = 0.0,
    mode = 0
    sample_variance = 0
    hash = [0] * 50
    mx = 0
    if len(input_list) % 2 == 0:
        median = (input_list[int(len(input_list)/2)] + input_list[int(len(input_list)/2 - 1)]) / 2
    if len(input_list) % 2 != 0:
        median = input_list[int(len(input_list)/2)]
    for x in range(0, len(input_list)):
        mean += input_list[x]
        hash[input_list[x]] += 1
        if hash[input_list[x]] > mx:
            mx = hash[input_list[x]]
            mode = input_list[x]
    for x in range(0, len(input_list)):
        sample_variance += (input_list[x] - (mean/len(input_list))) ** 2 / (len(input_list) - 1)
    standard_error = (sample_variance**(1/2))/(len(input_list)**(1/2))
    margin_of_error = standard_error * 1.96
    return {
        "mean": mean/len(input_list),
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_variance**(1/2),
        "mean_confidence_interval": [mean/len(input_list) - margin_of_error, mean/len(input_list) + margin_of_error],
    }
