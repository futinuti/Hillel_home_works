from my_module import *
import random as rnd


# проверка фунций на работоспособность
r = 5
m_na_m = [[rnd.randint(1, 99) for _ in range(r)] for __ in range(r)]

visioner_array(m_na_m)

visioner_list(adder_columns(m_na_m))

sorter_last_raw(m_na_m)
visioner_array(m_na_m)

sorter_columns_up(m_na_m)
visioner_array(m_na_m)

sorter_columns_down(m_na_m)
visioner_array(m_na_m)

m_listik = [rnd.randint(1, 199) for _ in range(11)]
visioner_list(m_listik)
sorter_selection(m_listik)
visioner_list(m_listik)

m_listik = [rnd.randint(1, 199) for _ in range(11)]
visioner_list(m_listik)
sorter_by_insert(m_listik)
visioner_list(m_listik)
