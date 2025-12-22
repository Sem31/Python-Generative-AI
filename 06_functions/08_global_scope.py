chai_tpye = "Plain"


def front_desk():
    def kitchen():
        global chai_tpye
        chai_tpye = "Irani"

    kitchen()
    print(f"Inside front_desk: {chai_tpye}")


front_desk()
print(f"Global scope: {chai_tpye}")
