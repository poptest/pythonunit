# -*- encoding: utf-8 -*-


class LiRunJiSuan():

    #TODO 获取并判断用户输入的有效性
    @classmethod
    def __get_user_input(cls,zlr):
        user_input = zlr
        try:
            user_input = int(user_input)
        except:
            print("请传入正确的总利润数值：数字（万）")
        if user_input < 0:
            print("请传入正确的总利润数值：正数（万）")
        return user_input

    #TODO 根据用户的输入计算对应的奖金
    @classmethod
    def __jisuan_jiangjin(cls, jiangjin):
        if jiangjin >= 0 and jiangjin < 10:
            sum = jiangjin * 0.1
        elif jiangjin > 10 and jiangjin < 20:
            sum = 10 * 0.1 + (jiangjin - 10) * 0.075
        elif jiangjin >= 20 and jiangjin < 40:
            sum = 10 * 0.1 + 10 * 0.075 + (jiangjin - 20) * 0.05
        elif jiangjin >= 40 and jiangjin < 60:
            sum = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (jiangjin - 40) * 0.03
        elif jiangjin > 60 and jiangjin < 100:
            sum = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (jiangjin - 60) * 0.015
        elif jiangjin >= 100:
            sum = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (jiangjin - 100) * 0.01
        else:
            pass
        return sum

    @classmethod
    def jisuan(cls, zlr):
        lirun = cls.__get_user_input(zlr)
        jiangjin = cls.__jisuan_jiangjin(lirun)
        return jiangjin
