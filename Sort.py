# -*- coding: utf-8 -*-

def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    
    #配列の左端と右端を参照する変数をそれぞれ定義
    first = 0
    last = len(array) - 1
    
    while(True):
        
        #左から探索する、基準値以上の値を探すため、firstが指す要素がpivot未満である限り
        #firstをインクリメントし続ける。firstが配列サイズ以上にならないように注意。
        while(array[first] < pivot):
            first += 1
            if(first >= len(array)):
                break
        #左側から探索したときと同様。lastが0以下にならないように注意。
        while(array[last] >= pivot):
            last -= 1
            if(last <= 0):
                break
        
        #firstとlastが衝突しているかどうか確認
        if(first < last):
            #衝突していない場合には値を入れ替える
            tmp = array[first]
            array[first] = array[last]
            array[last] = tmp
            #この時にleftをインクリメントしなくても次のループで行ってくれる
            
        else:
            #衝突している場合、lastが現在指している要素とそれより左は全てpivot未満
            #pivot未満の値しか持たない左側の配列とpivot以上の値しか持たない右側の配列を
            #それぞれsort関数を再帰的に呼び出すことでソートを実行する
            #それぞれの結果を+演算子によって結合したものを返す
            #配列のスライスについて、左側の配列にlastを含めるために+1することに注意
            return sort(array[:last+1]) + sort(array[last+1:])
    

    # ここまで記述

if __name__ == '__main__':
    main()