
# 参考: https://qiita.com/fkubota/items/53d9b58acce4afa10046

import builtins
import types

def imports():
    for name, val in globals().items():
        # module imports
        if isinstance(val, types.ModuleType):
            yield name, val

            # functions / callables
        if hasattr(val, '__call__'):
            yield name, val


def noglobal(f):
    """ノートブック上の変数宣言を関数/クラスとは無関係にするデコレーター

    Examples:
        @noglobals
        def test():
            pass

    References:
        https://gist.github.com/raven38/4e4c3c7a179283c441f575d6e375510c
    """
    return types.FunctionType(
        f.__code__,
        dict(imports()),
        f.__name__,
        f.__defaults__,
        f.__closure__
    )


if __name__ == '__main__':
    def test():
        if 'hoge' in globals():
            print('関数内で、hogeが存在する')
        else:
            print('関数内で、hogeが存在しない')

    @noglobal
    def test_noglobals():
        if 'hoge' in globals():
            print('関数内で、hogeが存在する')
        else:
            print('関数内で、hogeが存在しない')

    hoge = 'aaaa'
    test()
    test_noglobals()