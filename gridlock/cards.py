
from gridlock.board import Board
from gridlock.pieces import PIECES

class Card:    
    def __init__(self, info):
        i = info.index(':')
        self.name = info[:i]
        self.start_board = Board()
        info = info[i+1:]
        for i in range(0, len(info), 3):
            letter = info[i+2]
            piece = PIECES[letter.upper()]        
            x = int(info[i])
            y = int(info[i+1])
            self.start_board.place_piece(piece, x, y,letter.islower())  


CARDS = [
    Card('01:17A46b32C'),
    Card('02:62A13b50c'),
    Card('03:35A24b02C'),
    Card('04:10A67B52C'),
    Card('05:64A25B13c'),
    Card('06:76A65b25c'),
    Card('07:70A41b21c'),
    Card('08:07A21b31C'),
    Card('09:54A35B13C'),
    Card('10:17A23B20c'),
    Card('11:00A20b53c'),
    Card('12:00A20b53C'),
    Card('13:15A50B00C'),
    Card('14:46A41B00C'),
    Card('15:32A56b75c'),
    Card('16:64A13B00C'),
    Card('17:37A34b05c'),
    Card('18:45A63b10C'),
    Card('19:35A45b01C'),
    Card('20:77A24B37C'),
    Card('21:73A43B20C'),
    Card('22:12A54B20C'),

    Card('23:35A23b45C'),
    Card('24:56A45b52C'),
    Card('25:24A50B00C'),
    Card('26:36A42b70c'),
    Card('27:50A24B01c'),
    Card('28:05A00b30c'),
    Card('29:43A00b42C'),
    Card('30:52A30B13C'),
    Card('31:33A50B43c'),
    Card('32:42A02b53C'),
    Card('33:47A32b23c'),
    Card('34:55A50B32c'),
    Card('35:54A05B52C'),
    Card('36:35A20B23C'),
    Card('37:75A50b40c'),
    Card('38:64A37B50c'),
    Card('39:75A20B23C'),
    Card('40:44A23B45C'),
    Card('41:36A04B30c'),
    Card('42:73A50b45c'),
    Card('43:44A31B01C'),
    Card('44:55A31B01C'),

    Card('45:63A25B00C'),
    Card('46:52A30b42c'),
    Card('47:44A27B50c'),
    Card('48:31A34b30C'),
    Card('49:44A30b70c'),
    Card('50:31A24b30C'),
    Card('51:70A27B03C'),
    Card('52:42A22B03c'),
    Card('53:24A47B30C'),
    Card('54:34A63B02c'),
    Card('55:32A43B40c'),
    Card('56:23A04b54C'),
    Card('57:31A02b30C'),
    Card('58:42A04b37C'),
    Card('59:36A03B37C'),
    Card('60:25A43B50C'),
    Card('61:45A50b22c'),
    Card('62:52A30b45c'),
    Card('63:42A43B04C'),
    Card('64:45A53b30c'),
    Card('65:31A44B41c'),
    Card('66:33A40B27C'),

    Card('67:25A63B00c'),
    Card('68:23A50b73c'),
    Card('69:34A50b73c'),
    Card('70:45A20b05c'),
    Card('71:42A24b70c'),
    Card('72:33A27B00c'),
    Card('73:45A25B75c'),
    Card('74:65A34B75c'),
    Card('75:65A30B75c'),
    Card('76:22A50b37C'),
    Card('77:43A30b00C'),
    Card('78:44A34b30C'),
    Card('79:23A33b37C'),
    Card('80:35A44B75c'),
    Card('81:52A65B00c'),
    Card('82:24A42b37C'),
    Card('83:33A50b27C'),
    Card('84:55A27B24c'),
    Card('85:52A33b45c'),
    Card('86:53A03b02C'),
    Card('87:55A70b03C'),
    Card('88:51A73b50C'),
]