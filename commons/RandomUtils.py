from random import choice


# 高级选择. 根据 flag_config 从 sample_array 中随机选择一个值
# flag_config 形如 1,1,1,0,0,1
# 如果配置长度不够, 则默认以 0 代替; 如果长度超长, 则超过的部分将会被丢弃
def super_choice(sample_array, flag_config):
    if flag_config is None or flag_config == '':
        return choice(sample_array)
    flag_array = list(flag_config.replace(',', ''))

    result_array = []
    for index, sample in enumerate(sample_array):
        if index >= len(flag_array):
            break
        if flag_array[index] == '1':
            result_array.append(sample)
    return choice(result_array)
