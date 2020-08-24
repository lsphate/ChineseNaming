first_char = 8
second_char = 0
third_char = 0

san_cai_map = {
    1: 'L',
    2: 'L',
    3: 'F',
    4: 'F',
    5: 'E',
    6: 'E',
    7: 'M',
    8: 'M',
    9: 'W',
    0: 'W'
}

san_cai_pair = ['LL', 'LE', 'ME']

sub = ['LF', 'LW', 'EF', 'EE', 'EM', 'MM', 'MW', 'WL', 'WM', 'WW']

negative = [
    2, 4, 9, 10, 12, 14, 19, 20, 22, 26, 27, 28, 30, 34, 36, 38, 40, 42, 43, 44, 46, 48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 66, 69, 70, 71, 72, 75, 74, 76, 77, 78, 79, 80
]

positive = [
    1, 3, 5, 6, 7, 8, 11, 13, 15, 16, 17, 18, 21, 23, 24, 25, 29, 31, 32, 33, 35, 37, 39, 41, 45, 47, 52, 63, 65, 67, 68, 73, 81
]

female_avoid = [21, 23, 33, 39]

six_stroke = [
    '丞', '亦', '伊', '帆', '安', '宇', '旭', '竹', '羽', '至', '因', '全', '光', '任', '同', '臣', '存', '而', '合', '妃'
]

seven_stroke = [
    '君', '辰', '更', '貝', '岑', '采', '初', '希', '吟', '彤', '伶', '杏', '妤', '孝', '杉', '孜'
]

nine_stroke = [
    '冠', '俐', '妍', '俞', '映', '彥', '奕', '怡', '韋', '姜', '芊', '敘', '柔', '祈', '品'
]

ten_stroke = [
    '倩', '凌', '夏', '奚', '娟', '娜', '容', '家', '宸', '庭', '恩', '席', '晉', '晏', '桐', '畔', '真', '耘', '紜', '紋', '軒', '育', '珂', '恒', '恆', '祐', '純'
]

twelve_stroke = [
    '涵', '惠', '婷', '寧', '雅', '喬', '絢', '晴'
]

for x in range(1, 21):
    for y in range(1, 21):
        second_char = x
        third_char = y

        tian_ge = first_char + 1
        ren_ge = first_char + second_char
        di_ge = second_char + third_char
        wai_ge = third_char + 1
        zong_ge = first_char + second_char + third_char

        if ren_ge in positive and di_ge in positive and wai_ge in positive and zong_ge in positive:
          # if ren_ge not in female_avoid and di_ge not in female_avoid and wai_ge not in female_avoid and zong_ge not in female_avoid:
            san_cai = san_cai_map.get(ren_ge % 10) + san_cai_map.get(di_ge % 10)
            if san_cai in san_cai_pair:
                print (second_char, third_char)
