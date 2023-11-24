

#       / Параметры скрипта /
modules = list()
wallet_mode = 2  # Режим кошельков: 1 - порядок как в файле, 2 - случайный порядок
wallets = open('wallets.txt')  # Файл с приватниками и адресами бирж
log_file = 'LineaSwapper logs.xlsx'  # Файл логов
gas_price_limit = 40  # Лимит цены газа в Эфире


#       / Параметры биржи /
api_key = ''  # Ключ API основного аккаунта биржи
secret_key = ''  # Секретный ключ
pass_phrase = ''  # Пасс-фраза

exc_withdraw = 1  # Вывод с биржи на кошельки: 0 - выкл / 1 - вкл
exc_deposit = 1  # Депозит с кошельков на биржу: 0 - выкл / 1 - вкл

exc_mode = 3  # Режим вывода средств с биржи: 1 - часть от баланса | 2 - весь доступный баланс | 3 - число в ед. эфира
exc_percent = [0.3, 0.4]  # Процент баланса, который будем выводить с биржи

exc_sum = [0.28, 0.34]  # Количество эфира, которое выводим с биржи
exc_sum_digs = [3, 5]  # количество знаков для округления суммы вывода с биржи

exc_limit_max = 2  # Верхняя граница суммы вывода с биржи при выводе процента от баланса (в единицах эфира)
exc_percent_step = 0.05  # Шаг, с которым уменьшаются границы процента баланса

deposit_remains = [0.0003, 0.0004]  # Остаток на кошельке при переводе на адрес биржи (ETH)
deposit_digs = 5  # Количество знаков после запятой для остатка на кошельке

exc_digs_min = 4  # Минимальное количество знаков после запятой для суммы вывода с биржи (при % от баланса)
exc_digs_max = 5  # Максимальное количество знаков после запятой для суммы вывода с биржи (при % от баланса)


#       / RPC сетей /
ethereum_rpc = 'https://1rpc.io/eth'
linea_rpc = 'https://rpc.linea.build'
arbitrum_rpc = 'https://1rpc.io/arb'
optimism_rpc = 'https://1rpc.io/op'


#       / Параметры модулей /
switch_bridge_exc = 0  # 0 - Вывод сразу из Linea на биржу | 1 - Бридж в Arbitrum, затем вывод на биржу


#       / Параметры перерывов /
bridge_delay = [10, 15]  # Перерыв после поступления средств в сеть назначения
swap_delay = [5, 20]  # Перерыв после свапа
wallet_delay = [15, 100]  # Перерыв между кошельками


#       / Параметры бриджа /
bridge_sum_mode = 1  # 1 - Бридж всего эфира, 2 - Бридж процента от баланса
bridge_sum_percent = [0.015, 0.021]  # Процент, который бриджим
bridge_sum_percent_digs = 3  # Количество знаков для процента
bridge_sum_digs = [4, 6]  # Количество знаков после запятой для округления суммы бриджа
random_mult = [1.15, 1.20]  # Минимальный и максимальный множитель цены газа для транзакции бриджа

#   Старгейт бридж
net_bridge = ['Arbitrum', 'Optimism']
slippage = 0.010  # Проскальзывание для бриджа (например: 0.005 = 0.5 %)


#       / Параметры транзы /
gas_price_mult = [1.05, 1.10]  # Наценка на газ
gas_mult = [1.25, 1.35]  # Добавочный процент для количества газа


#       / Параметры свапов /
work_mode_swap = 0  # Порядок свапов 1 (USDC первый) или 2 (wstETH первый), 0 - рандом

USDC_volume = [510, 550]  # Количество USDC, на которое мы свапаем эфир за первый шаг
USDC_txn_count = [2, 4]  # Количество транз, за которое свапаем эфир на USDC (рандомится от [x1 до x2])
USDC_switch = 1  # Включен ли модуль USDC свапов

wstETH_volume = [27, 35] # Стоимость эфира $, которое свапаем на wstETH за первый шаг
wstETH_txn_count = [1, 1]  # Количество транз, за которое свапаем эфир на wstETH (рандомится от [x1 до x2])
wstETH_switch = 1  # Включен ли модуль wstETH свапов

slippage_USDC = 0.010  # Проскальзывание для свапов USDC (например: 0.005 = 0.5 %)
slippage_wstETH = 0.030  # Проскальзывание для wstETH (например: 0.005 = 0.5 %), меньше 0.030 не ставить, т.к. не проходит транза
swap_sum_digs = [4, 6]  # Количество знаков после запятой для округления суммы свапа


#       / Параметры для работы скрипта /
exc_remains = [0.000003, 0.000005]  # Запас эфира при переводе на адрес биржи и бридже (ETH), чтобы точно прошло
rem_digs = 6  # Количество знаков после запятой для остатка на кошельке
test_mode = 0
last_row = 1
gas_price_ether = 999
stop_flag = False
start_flag = False
