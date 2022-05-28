# -*- coding: utf-8 -*-

def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    
    #left, rightは探索範囲の配列の左端と右端を表す
    left = 0
    right = len(sorted_array) - 1
    
    #探索中、探索範囲の中央のインデックスを参照しながら
    #left,rightの値を更新することによって探索範囲を狭めていく
    #target_numberに一致する要素が配列に含まれない場合、
    #最終的にleft > right となってしまうため、その時にループを抜ける
    while(left <= right):
        #int型にキャストすることに注意
        mid = int((left + right)/2)
        if(sorted_array[mid] == target_number):
            return mid
        
        elif(sorted_array[mid] > target_number):
            #midより右側にはtarget_numberは存在しないためrightを更新
            right = mid - 1
        else:
            #midより左側にはtarget_numberは存在しないためleftを更新
            left = mid + 1
    
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()