class PhoneNumber:
    def __init__(self, number):
        trimmed_num = ""
        for char in number:
            if char.isdigit():
                trimmed_num += char
        if len(trimmed_num) == 11:
            if trimmed_num[0] == "1":
                trimmed_num = trimmed_num[1:]
        if len(trimmed_num) != 10:
            raise ValueError("Invalid length")
        if trimmed_num[0] == "0" or trimmed_num[0] == "1" or trimmed_num[3] == "0" or trimmed_num[3] == "1":
            raise ValueError("Invalid - 0 or 1")
        self.number = trimmed_num
        self.num_list = list(trimmed_num)
        self.area_code = trimmed_num[0:3]

    def pretty(self):
        return '({}{}{})-{}{}{}-{}{}{}{}'.format(self.num_list[0], self.num_list[1], self.num_list[2], self.num_list[3], self.num_list[4], self.num_list[5], self.num_list[6], self.num_list[7], self.num_list[8], self.num_list[9])

