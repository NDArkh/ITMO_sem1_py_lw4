from random import choice
from random import shuffle
from tkinter import *


class KeyGenApp:
    def __init__(self):
        self._wdw = Tk()
        self._size = {'width': 1200 // 2, 'height': 625 // 2 + 68}
        self._bg_lbl = Label(self._wdw)
        self._init_window()

        self._key_0 = StringVar(value='******')
        self._ent_key_0 = Entry(
            master=self._wdw,
            width=100,
            font=('Consolas', 18),
            relief='solid',
            bg='black',
            fg='DeepSkyBlue',
            justify='center',
            textvariable=self._key_0
        )
        self._btn_generate = Button(
            master=self._wdw,
            text=">>> GENERATE <<<",
            font=('Consolas', 18),
            width=100,
            relief='solid',
            bg='black',
            fg='DeepSkyBlue',
            command=self._on_click
        )

        self._pack_all()

    def _init_window(self):
        self._wdw.resizable(False, False)
        self._wdw.title("X-key gen")
        self._wdw.iconphoto(False, PhotoImage(file='key.png'))
        self._wdw.geometry(f'{self._size["width"]}x{self._size["height"]}')
        self._wdw.configure(bg='black', relief='flat')
        # we need this trick. trust me... or just try to run without it
        self._bg_lbl.image = PhotoImage(file='bg.png').subsample(2)
        self._bg_lbl['image'] = self._bg_lbl.image

    def _pack_all(self):
        self._bg_lbl.place(x=-2, y=20)
        self._btn_generate.pack(anchor='w', side='bottom')
        self._ent_key_0.pack()

    def _on_click(self):
        if len((val := self._key_0.get())) != 6 or not val.isdigit():
            self._key_0.set('******')
        else:
            self._key_0.set(self._generate_code(val))

    def _generate_code(self, base_val: str) -> str:
        # XXXXX-XXXXX XXXX	1 и 2 блок должны содержать 4,5,6 и 1,2,3 цифры
        # введенного числа соответственно, остальное - случайные буквы,
        # 3 блок - результат сложения чисел, получившихся в 1 и 2 блоках
        tmp = [x for x in base_val[3:]] + [self.random_alpha() for _ in range(3)]
        num1 = int(''.join(tmp[:3]))
        shuffle(tmp)
        result = ''.join(tmp) + '-'
        tmp = [x for x in base_val[:3]] + [self.random_alpha() for _ in range(3)]
        num2 = int(''.join(tmp[:3]))
        shuffle(tmp)
        result += ''.join(tmp) + ' '
        result += f'{num1 + num2:>04}'

        return result

    @staticmethod
    def random_alpha() -> str:
        return choice([ch for ch in 'qwertyuiopasdfghjklzxcvbnm'.upper()])

    def run(self):
        self._wdw.mainloop()


if __name__ == '__main__':
    KeyGenApp().run()
