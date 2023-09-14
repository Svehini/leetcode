value_dict = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        skipNext = False
        rom_list = list(s.strip())
        for i in range(len(rom_list)):
            if skipNext == False:
                skipNext = True
                if i == len(rom_list)-1:
                    total+=value_dict[rom_list[i]]
                elif (rom_list[i] == "C") and (rom_list[i+1] == "D"):
                    total+=400
                elif (rom_list[i] == "C") and (rom_list[i+1] == "M"):
                    total+=900
                elif (rom_list[i] == "X") and (rom_list[i+1] == "L"):
                    total += 40
                elif (rom_list[i] == "X") and (rom_list[i+1] == "C"):
                    total+=90
                elif (rom_list[i] == "I") and (rom_list[i+1] == "V"):
                    total+=4
                elif (rom_list[i] == "I") and (rom_list[i+1] == "X"):
                    total+=9
                else:
                    total+=value_dict[rom_list[i]]
                    skipNext = False
            else:
                skipNext = False
        return total
