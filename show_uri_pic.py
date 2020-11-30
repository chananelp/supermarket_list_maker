# https://stackoverflow.com/questions/33754935/read-a-base-64-encoded-image-from-memory-using-opencv-python-library
import numpy as np
import base64
import cv2


def readb64(uri):
   encoded_data = uri.split(',')[1]
   nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
   img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
   return img

data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFwAAACMCAYAAADx0c53AAA0P0lEQVR42u29d5Bl2X3f9znh3vty5+7JcWewu1gsgF0kkiAl0RJLJMRQlEzZFGzTcolBLFOiKdsyKUtyWSW6FGxRZdoky1TxDxE0JchMoBgACgRhEIslVtjF5jA7qXN+8cZzjv8494WemQXE7kEvqzy/qrfd++b1fed8z+/8zi8f4ZxzPKBjI/l2D+D/b/QA8GOmB4AfMz0A/JjpAeDHTA8AP2Z6APgx0wPAj5keAH7M9ADwY6YHgB8zPQD8mOkB4MdMDwA/ZnoA+DHTA8CPmfRxfMlkjMP/OvH/5U8x8V/E6Lc7SCDEvZ5/8Jnj9w5+i+Pgc8XEw4S49zfebxL3M+IzfNTwiULcG6A/qeQcOBw4EOJrswj3BXDn3FsOzhpDkqQM4pQkyWh3esRpTpoWdLt90izHGEeaZvQHA9IsxzkQCPLCUuQGWxjyvMA6h8OhpEApiZACHGilUFohBBTWInFIKQgCRaA1YajRgaJeq1CtRFQqIc1GnWajQr1Ro9WoU6tXkVL9seb2tgEOkGU53W6PbqfL7eUNbi1vs9/pM+jHxElOluUEWlEYQ2EsURigtUQpgVYKLSU6kCit0EoBDmsMeVZ4sK1FKUkYaKIoREiJcw7nHMYYjLEIAdZBXhhwoLQH0FhHYSx5lpOXi2cKS2EKsrygGgVEUcj0VJ1zZxa5fOksM7MznDy5QBgG9w3s+wb4m2+8ydraGt1ezK3lXfbbA5TShKFCCoiigGoUgnBIKbHGevEjQCuJUqoED6yxWOc89wJFYdAl9wohUUqipEQIgSw/Y60rORGklEjl/51SthfG4qx/plSSIjcURYHWGmMshTHESUZ/kJBlGZEWnFiaolGr88hjj3D+/Jn7xumHBnw4gG6nyz/4hz+HDhtcPL/A9HSN8+cWCLVkMIhRUpUTysmzgjTNAYHD//2QU/OswBiLMQYpJUGgCaMAWYILAmM91yMERWGx1iKlFz9CCgLlwZZSgnA46xc4TTKMMV4MCUegFVEYABYdaPIsRWtNrV6j08945Y1NVtd6vHpjm/Mnmvyj//mvIpU6DEx30aG1lCHg6+s7/OqnXuT12wkyl8xPVVk8Mc3pMzM06gHnzy5RmJT5VsTps4sECrJ0gBRQq0YoWXKxUuSFJSkkcWoIAgHCghBICTOtKmGgMUIgnKOf5OzsdnAOwkAjhUNJiEJFmhmkUjQaEUWakhWOMAqp10O2NtvstvvIoM6t1R0MATdvbBGnkr1OztryPnvdHIPARXD2XJv/bmufxRNz94XLjwC4/7m6ts3KXoKaqmHSgo00ZuONLi9fXwetkPYlwiikUguJKhHInFatyuzsLEo48iJF6RARBNgC8tSSFV4EBFIipEJJqFQUQRigAo01BmMtTmrSzBApRZYXGGtwUhBFERQxoYJK0CRXEusE+/td2r2YQlZI0y063T5pYZGEZHmGSWKIalBPaFUdUb3Kxn6f7b0eiyfmsNah1NsE+JB22gP6SYGKLLIwqFaLIApxcQeEROFQIkdFIUWRYJxjJ+uztdtFCrBO4YACSWHAOklmHVJoTGG9HA4CtBVILEmWoSs1GrUqzloclhxLpBW1ShWkQMkUawqsk1QqfpfkRUFRFCityW2KFApdC0uu1WgbkJgqzgmKgaXbXqPW2ULNP8Z2Ox7tai/GDm8vHhnwjY09QCOURNQCbNIhTSVRpV4O0JAbS95PUEpjnaMoUiQCWR6WAoENNIWzOAk4g65VUKZAOlChRqsQWWTIzBA1QkIdlKJJ4grIbIrMJZkQKGtAarAZsXUUWY4OA7I8Qyi/hoVJETrEWYctYoR1EFVw+5tEkaY6N4Vb/iInuMAn/90LrK60+Y5vfTe1WsWrrYdk9EMDPvzCc6daPPLQLDe3U7JcQ7UCRYYxBU4Ir02oEOdypNSYPPOHpQpAKmx5sJkixQoN1uAc5LnBZglCaiIVYG2OSVPSLMWpiFwLLBIpBAhJXjiUNFilEQgUDisE2MKrnxJCKcldQagDpNRYYf33RyHWgctj6uevom49j72xTnrizyBNnX/6Tz8FxQqXzy3yL37hx3n/k5fLcf/xUT+CL8V/WZbGiH4Kq31UpyAcFOhcEgAKgRJeu3AW0jwjyw15LilyQZ5kuLTwWoSVSOFltghCb94LkFqhgoAwqqCrIboaIQKvNyuliKKQaiUiiKpIJamFEUFYxZU6N8ZirCPLcpxUCCfAgstysjjHWEPezyi2OpjdmO4rr9G79Txx9zN0X/+/mVY3+fG/8x/R3vgY73viAn/l+/6JB04KDqPeHZrDpRQYU/DyKzfI0AwyiRgUUBQI57CBREUhuioIKg4x1cBJw+nFCrPzc+xsrOOsIqi16MSwu9emSGOQAi0ltrDYzOCUZdBPUVENTIEtcuLODoWOUMKQYlFBRO4gw+JcB1FrsLg4T8sOYNClOTVFa+Ek/W6P7Y119lSFJHfIJIGoju10oRCIAhARxj2KUhGqGtG3U8zPNAkqTX7u53+c9a32HSx3TIADKCm4vbbL7naH+nxEhkAUDpM7CiExBcSuQBDi4pwgVMw6zbRwLJ5ZwDhIrWInHZA5jSgcGEUhA1wicanBCAGZwRSpn6TW/hBUUIgQpxV5JCGUUJW4iiaMFFOh4sqJswjjRZjWir08Qi+eobexR5I5rBOwvYWwEmGs96PYDNeoUvA4CMHO/oBmZEcAnz05exTIjqYWCqFo1Kvs3txDUsVKEFGAqHjRQBSgyBBK4/KMUFUwSnBt5RaLi4vYqML6xg6D9S3IJE40QAhs1keYAuFySA1OKKQCJzWg/JcXBU5LIIBCIcIAKauIUNEwCd2tLi+bDrpepykVJtklFordTp+WdFSqFjFVxbUqdDsxRe4w1kFaQFYg+hk2ziG01OuVcldLrHP+3Dh+wL0R8MjVs0StiCzVBKHCSY1LC5zJcTaHSEOvD0qQZbDWXsWSsr8vqVQ0g2RAupsibAUZOYyyCGu9nA0CcBqU8k4SORyuAKERWuCkAilRhSbKNSoDiSRHYbYT8nZBt1KlSHLSIqfILC63ZKnB6cKLrUGGyAzKAbHxmktugRzt5MgnAxwJ7CMBLqUgTRMee+d5/vxH3sMfPHWb/V6G6yfglN/iSoIUyECXMt+b5eQhO5v7CCWQtQCjq4gEzP4+0koQCmcVOG/Se4y99oF15VvK464sAosRBQMdg7O4SOAqGmoRItQ41/O7IgggLyApEEGAEwrafcidf+7AgAEkVKYjTp6e5iPf9hAXzy/Q7/eo1xtHAhuO6LxaXr5JmgzI85RbK3u8/OYur1/f4dZKh9XVNrv7A3Y2OvTTHKlC8rhN6/Qc588usH7jBlOtKRozs9za2GV3uw0mgNhBXEDmfS7IKjjrXyIoF2G07F7PqgnILUgJrQpUFCiJqEToSoUQhxQOKxSZceTGG0PCOuqRYr6umZ2qsTgVcvp0k4fPNnn48hSzU4q5qSpRpYkOIk6dOn0ko+dIgMfxgPX1Zfb29kiTlEolotmoEkUB1oGxMIhz+nHB1k6fOHVs7XTop4ZACrp7eyhdITeCW+ttttsxnTSnm0PSzRnsdbHGoVSEyy3kBRaFURppHFoaZBhQm25QrQYEkSZs1nF5TKWmaU3XaEaamtJoaZmdCmk1awghqNcDms2IwBUszNVoVhXVaOyPMcbS6yfEcUaSpjQaVebmFpidnaPVmjoS4IcQKT5QlcQD4oF/BUGIBfqDjEFcIKVEaUkUKOrVkNOLTaQUKHUWARhrMc5786x1gERpTRRopFJ0ejE7ux129/qsLK8TZ4ZOp088iElygykKAiURQKAVjWaVM2dPUqsEzM80WZhrMTvb8o6tMEAHAdZaBoMeWZYihcQYi3VQGIsxjiTJMcZgbenFFJIgDEFI4jghTRPiOH47ABc450jSmMFgAEKglCLUAUKAUspvVyG9OzU35Ln1yyQlUioW5heRUhLHA9IkxtqCwSDhxRurvPLydVZWNul1B6RZxuZ2hzjJ/TdLQb87wDjnQbOlXx1Js1lndm6KWrXCwuIs/8VHv4PHH7uMMaWHT0C1Psvm1hb7e7tIJUfzEQK01qW4cKPABoBzijyXJElCnmdvjy/FWkMSxyRJgtYBUpUnuXMlqBKBGA3M4dBBiDWWxcUTNBpNnHM0m00Ggz5fePoZnvrDL7OxsU23F2OMQyuFkJoTS7OYwmCdJc8L8mYV57wNgNTkxlGrhlSrVZqtOkprpJL86ic+w95emw9//XuQUmCtRWvBqZNLSAGdTrv0tYO1Fmu9v3wI9vCllF+MOE7I83zkrz9mwC29boc8z6lWa0RRBSkEUkvSNAUHURQxGAyQUlGtVdja2GRp6eQIbBysrK7we7/3OV54/nWE8G7VPLMo5YgiSZKmWCcIqiH92LC/30MrQb1Zw+FIkgHzcy3q1YB2p8fNm23mFheoRAFBkPBbn/xD3ry+zHd/1zcz1WqUXOtYXFwgTROSJMY6wd5+j0olpF4NcM6WTjdASMCipCZO+qRpgrX20GAfGnCAQezDaMYU7O/t0W13yYvCxy0LQ154zSIMQ8IoYn+/y9lzlwAfDX/q81/gd37n9+l0evT6KXE8wNi8jADV6XZq3LwlGQxqpKkkjkP63QghHbVGjSC0hGFCve7QwT4q6NJoZGR2gJIBzXqTxaUZnvvyC+zt7vCX/uKf59SpRVS5A1tTM7x+fQ0hBVEQIFWEkyFaC5yz5LlBCDA2JapVyQpDnh9zAGJo7KRpQjwYeIeQtWitwBXYIgNdpVKJqClNFEUURUEcp7zj4aucOLGEMQUvvvAS16/f4MyZEyilKIoBGxtdvvhMjxdf1izfFsSxmBieAyxQAxyDAZT6YLmATcJIcPK0QGB58oka3/md78U6xebmPnOzTW6urJPkhqlmnempBjPTLR55x0N0en1EuWu19k6xLMsII4W1BikVSiosgjA8ehrPH0stHALebu/x7DNPI6WkUqvSbE6RZSlah5iiIMsy5uYWqVSrtNttBHDx8mXyPOfG9es+JaKf0GiEDOKEj3/8Or/8y6usrhYIIXDOG1Y+VgkgfOAZb15T5o8M5e/QOPIzEQRV+PbvPseP/c338ciVOTrd3KvxpegVCBr1Co1Gjb19vzNxYJ0lCgKyoiAKAqxzZHk+lunGcGJpjmq1eryA7+/v8vorX6bRnCIIfMoCDoIwKjlOonVApeIPuCgKMcbQ6/u8E1MUNJuK557b4cd+7DO88MIuQoSALv3sgiCQpKlDkOMApQKEcBRFgZSKMJQkScGVRxrcvjEgyzQIi3ACi8WZlMZ8lR/5G+/lx374/SglGQwKqtUQaz2Q4AgDnwahlKQovPzWergyfqGNtQghGfT7zEw3aTYbhw5CHArwnZ0tbt94ndnZOXQQ4KzDWEsQhKWaGFCyIUoH5HmGkgonNM5Zwkjwj//RZ/kn//hZ8kKjlD+srBUlhwsefjTk1s0e73vfGebnKzz/5VU+9PWLSBGRm4JqI+Q3f22Z7/nLp7h9O+VXPn4brSKMcyBBRRJXGEya8OQ3nOHnf/bP8eiVBfY6KaGWpb/da1KTwWHn3Fi7GqqHzuGAXq9Ps1mn1WzclTb3H0qH0m+MMQRBSFSpIYVPaahUKqMUBSkn80P8xIy1hIHAmJyPfvTj/ORPPo11YXnwelepEK5kLMcrL/V59LEqv/Sxb+GHfvB9KF1ByoA4SyhshhCay1eafPL3Xufam/tcvNyiMLnnOuswWYEzoOtVnvncKn/mIx/nV3/3NWanfHRHKYXWegT68DBVykeRVPm7Ugoh/U9bgu9X4zDIHTbi4xw6KPM6tEJINRq0UuMkHc81DqU0rWaVjY09vusvfpx/+5u3CIIW1gqMceVucODEyOCQMuSLX+jx5Rf2SbKCvc4OO7u7vP7qJm9c2+eVl1bY2u4w6GuWTkTUm973InCgBSKQOAkmteiZCu09w/f8Z7/JP/+FLzE7U/O4OTfi0iHwUpR5MEIghfQWspQ+nU4qDu95OgLg1lmU8nl7slx9KX1SzzCBc6hXW+tzTN64tspH/sIv8kdPbRIETYq8zJY6sDnFiHv8rna8eb3L3s4eGyvLDOKERmMKHUYILXHW8Df+6yf4pg9P88br3uq1ApA+B9HPUFCkFiEESkX82N/+f/mf/tfPUqsov0AlNw8ZaZR4VCKrRolI7r7kpRwK8CzJKIrC68x4k3uoAggYyT1rLcZYpMj5ib/7aa5diwnDOkVuSphlCcvYmBCULlknAMWtG9tcvFzlZ372o2TJFP2excSC69f6fOTbz/P5P7rBb//2FlmqvEgS5fOcLaMkIJx3SDnnUNWQv/+/PMXTX1qhVguGIx6BOVyoIeN4X085NsF4IY8TcB2Gpe9BlGY8oxdlpN6no+UopSkKWF02QIApTPlJW6p2kxP0rgEhQUgLBHz692/zE//jUyyvpbz/A6dpTXlx1Ws7siTg335ih899dgfnvNNMOIcTZURdCCiADEQhcInxQWQneenVLYQonWdi7IKAyYxZvxh+fAc5/7B0KE1eSUlQqlPjQbxVcrul2x2wt9ubWF9Rftri3HDL5iAU1haAz2cBydNPbSCE4w/+3a3xsooKQmp+5n9/GmsdH/zwJc6fq/OvPvYiKvSeSRvnICLP3g4orJftqQHrKGSIz1c0yNJDKEsbwJv3jL5PTHDUmOEPp6ccCnAhh44picMyOrKFODAEa7whY3KfruyTOIfcXe4EZ4kixff/tUf5tV9/nQ9+3WkW5qtcefgszz6zTK+bsrLW59y5Ju96/CQ60PyDv/+HTE3V+Tt/95tpdxI+97k3+NAHZjh/5v10uo4PfP1Zfve3r/PLv3gNpbUXWNZBUb4wJVerkSt2yDei9H56N20pRkrfj0DgRr6Uw8nyQ4kUVWolo6+dqHgYihQfKQ+QSmGsI8+HFuGQRSzOWbTSJEnC6kbCz/38t7K/X/B//h+v8++fXuNDX3eO7/+Bd/HXvv8xlm/3+fVfe5V4UPDYu04gNfQT+OLTN9BK8N/8zd+n2qyxcLLKP//fnmJ6WtNoVTCFLTlUgi1TmIViY22XybNjSEPnlQfaTrhqx+8dhQ6npViDHA6oBNoD7w+qg6qqA6kwjAOx483o9XOI+OTv3uDZL93mU797G2szbtzo4FzGJz7xMkkCtark5OkKt5c71GsBhXW0dwesr/cQaL7hG9/B5lqH6zf6XHxogWZd4AOUPvEHV4JtBRSW1c1OORc7AawdAzrBSUMROYzaH4UOJVKMMSMu8EHdknNLE9gx5Aq/PZWOyq8qwJW68h1rbazk5s09rFWAYnl1wLPPb/HZz2zw1BfaLJ7QvPj8HqfOCDbXYvq9nC/++w3WNgyFKFg6UeVf/uIbXLq6wGOPz7O6HtPrpAgZ4tSQGcAF/pC0cpz6MNyRUJoDpQiRUo3mMWIW+zYAnuc5asjV40IDSvViNHhrfTlIHKcYWx5AaqjyiZFWgxVkuWN1PUXpAOcCblzv8bM//Yqvu3FJWTGhufbGWmmWS377t64hZMCbNwY4Y1BRyAvPb/H8sxu4HGQY+TNzqP2lrkw2GmpKk+AN7Qc5EiF+eGKktUgpfPLQcQMuR4aAZcSpojxUnAWGMt4AXm/PBvuAxBpZihx5YNJZLPjVj7eBEEgZqgXWmPEXu7z8pcySQuLIys8qzCA+AKDNBiWHOEABEmkUFD7fEHwe+hjg4XiG6qEdjWPI+UfVww/p4HWjA3JcIylGMn0yqVQAutnk3X/72xiYEOkgywXdTh+6HURe4JwEJxGufJ7xKcxSlMVVIygcAonQ3m07VNeEkiA1zmaIUCIbDeozdcKK8mUnGKhXacw0aNUkfTSPng1JujFuaLAJgXOe80UZ6fFay8RiHJDfx6gWGmPRkUZKHw3HWZzwBsUwkDxUsWyeI8KQd3zXNzDw0h2HGCmT3robr44P4/oyE18VKEYWoEQgBWgpUfjjwwFqaJzi/17L8tluLDQkIJ1DAYmDZlSgVA75+DwSQo0OzxFTlfVIcijn345D05XOYKk1rigAb+FZWTqehMJisNYSBAEugazdxyCwk5q7mwC8NKWHZ5Qtz4hhatlQwdBCYKSgGDq5RBmkcH5xnD8SRn/jH+0BU0LghMA4QS58RELpscNstO7Dw6l8ipiY89sC+HAv+8i8Gk1NDFVCIRClbDdF4VMVVL38jECJsQY8skonJjl0fg3Bl2Ls4hJiuA08gOAz6pQU5KOcEj8OKYYSWI6MGCEEwvodZq0tnzmelpvcbhPvSTGMNB2NDgW4VmoY1Bpxx2gy5ctah1QK4QxSOl/r40qg7zFqUcqAoa3qnBchQ5JDzncOLQSBnNQyfBrE8BiWEyC6oQvWDcsUGdkKXn0d1+4MXcvjmn6Hc2Pv5/2gQwHui5OGutZ4YlByo3M4a3DOei6TikxH5EKM5C5CYEsjY6QLM2FkiFHB+4H1kUKQO+frgaxDK4FWEiF9YhDW4cqEHoSv3zTW+dwZ63MMXSgpRDoSaT5oMiFCRuCOF3XoWjkq7IdTC++obRkdLkPLE+dLR4zFAqq/z/kvfYlMaVSoKZxia3eXsNHERA1ykxEEIUZ4dVJqRWEkhc1BaEKtSIscgUBLmGpWaTSr1Ks1bJIibEG7M6BeDZhpVFDdNlUMMs1ItjdZWpwl3u2w/fKL3H75OV57+Q0qH/1P0P/9D1P0+gitGIuQu+d2QC8/YjLn4byFakJuj7begWF6bpU+Yb5Vj/jmOcfWxgZ72/tg4SGhUG4b0Q0IQk2ns0uW+gUz1hHVWlhX1hA54zVtWaHWqBGGkmYTTiwtoHXE7dVN4hTq1YjHFgUXZioMugP211awUlFce4MbT38eubXN65/9ApfPXWXp7DlMXoxKzMc432kQTb4/ecAejtcP5y0svXz3GuAoOgKYIitr63Nks0ZdCuRUnf12D4vASoUUgkwKavPzRFYQJxkuzbFhQLVapaGmcCYnTQp0EBCEPq973xTsrvSQOiYMWyRAPXDMzIbsFpZBnBNXGtRbDV751KcZDFJeePkNgivv4NEf+nsMZITJM4ZGzZjuBHtSnh9dDz9cAEJrr3tPOOqHh+VwUEophLNYUyAFnFqaQpmUPEtp1uu4bEAtMCgTo0xKIApqkaPZCFlYmKM11aLIEkySEAUhiwvzTDXrhFrSrAU0m03qjZbnGJNBf4/3ngAtLFm3Q9Ht0axV2Hr5FfZXV3ntS8+zY+DJH/pv6XY7qGyAKH0l9yr/G/lUJpnpjoU4FHaH+ivhtQJrCm8IOzuKiEzqsDIIwQmimiBd34Ii4+TJJTJjqDWq9Nu7pHmCiGo4USE3jizNiNMuQRBRDSPiQUynnRDHKc1GnTROiZMYpTWBDqlFinZ3wJOXmsy1IiwKWQjanQHtzQ2uPfc8bz73Am/stvnTP/GTdHOFTQZUavNlkOMtpzjyq9wZfjsKHdK0LznZ2ZFD3uGtTaXD0cHjnYmWIkuJ+z3OPHQRHKyvriGFYGphkdwK9noDsl6C1CGNSoN6VZMZQ+EsSEWeG5Sz5HkKwpFnhiiMSAc9un04N1Pj6qkWhRPs3LrFzo1lsk6P9Tde49rzL7LfT/ng3/p7uPoig90tZmfnyNMcpSR5aWnei4Y9WIbz9Xr72xBEHuafDE3g4WvsrB8eRN4nIaXk1NlTBBp2NleJu/sEIqcRSU6dPsWVi+c5Md2gToFIO6S9NiZJiAcxwlma9TpKWJ/XLaBeq2JNTqUacWmhypMX6xS2YOvaNdZeeo1ACbL2Pq89/wrtbpeHf/BHmb/wEC7dZ3Fpmt3NdXCTJv1YLIIXJ74Hi69U9unMdtQm5NgBFwhsqWcP3xn/Fw467v1EpmZm6Hf3OHX2DBeuXkWi2NncYHt9BVcktFpNnBQMkpRKrUagBbVQYrMBJm5j0gGBFKT9LirrUHEJTW14/FyL1nSN9vIWN595jubsNINujxe++CX2dna5+l/+EIsPP8r26jK1apVut0+1GnFyOqTIizt84eMg8tglO05moox7HoUOnR9uR6Kk9K4JwJoDZrk/lDKU1nTbbapRRLWi2VxZodvrElvf6affbyN1hfmFOV579U2sk1SrFQaDBGELpIi48o6LzM5MU69X2d/aYOWpp5g2CXvBJW7t91h77TVOXz1HbWqG537399ne2OKJv/63qFx+lLQ7oFap048LZJHygfMNzp9qInSANUXJHMODspzVSJQMf3qOl/JoLZkOqRZKpFD+UClBBomdyGL1ByllmkTO6soKs/PzdDoJQVhhYSFkv92jNTOLs5b+IKY7KDhx7gI2Sbh94ybvfvdVvuEbnySIKhRZUprZAqGg/573sfzZz/Dmv/4V8iRj6tRJdKXJFz/5B7z48jUe+c9/GH3mMi4ZkJR+8dNThveeW6SqJS4IyuwwfYC7PfCTxk5ZhTw8l94Ow8c5h3V2tM28V8f60JkDKP/NCYRUFFmXWq2CLTKarTrVWpWVm7eYn28SJwMCXWZohYqZag1br6GF5cN/+kM0m3XiXocs7mGcI6rUETbn7MXTLF34Pp7/rd9g7wtfIE8Nn/y//iXbnR3Ofvf3MnXhEnG3TSe1RErz5EPTXFqqEPcGYEGW5SN6QqRMsNR4DpMW6NGVlMOnSYjSzSbuiNyMgxJeVZRSElaqpHFKksScm5tjd3uL5sw0W2ubbG7vE0VVLl+9xP7ePjs7bS5dOok+X6ESBWRpgsASVSO6nR7YnDSNqbdCRN7j/Ps/wPTlR5BS0FpbIZqbJZUttte3CULJbA0evzDFiWlNEg/I8pTtZ56laM3ynnd/EJumd2TPghcpQ06+DygfGXDG6QLjgVqEUBPvjWOBSoUILQlUwCsvvEC1GqJ1RBb3ESpAKs366gpxt0O9NcvZc6fQQcCg36FWreCEIqxE9G5dJx1EVGt1hImJtGZpsUUgLdvbXWYfvkLg4PatLdxgnyunlrhyboZQQXt9h/72JvHGBp/5xX/NpW//Dj6kNYM0PcDhYxft+AAdz2mc/HlY7fCQzquSqydOc6GCEVdMTsCVLfFOnzvHjddeJU0S8jgmqtY4deEU7vYGtVqFPBlw4cplzl+6QJEOsDIkjftIJdC6QjzocursJdI08+5epYnjlKgSoJWk0aySD3pkTjHXCKm+eYPL8xformzRWJxm4+VXePlTn+bWjZtsFwGPXn4Ec1dq22jUd7LXOAAh7tTIvoaAD79E6/KkLqM+Y6D9p1wp30fGghCs3LhFWK0TxRmddo9qS6NVQKPZQucJjdefJ9vbRF+5yGDQIZipMruw5EsEdYgzOVG1Srd7C+EcrZl5VO5I4ozmdJM8WWdrc5VKdYZFZXjp2efYu3mNS1cv0qyF/MHHPsHWXgf5+Ad577d+OzNXH8Ok6UTG70HH1Dgx39sV4wys44z4DH3Vqkz1lUOw73TklGphafggBOmgT1ip05qd49q128RpzKXLF7nyjvNcf/U66eIJEmvp97sIrTFZmyBaAmuxRYFSku7+DpVKA2MdxvqUhc7eLoGWhBWNcIpGf52ku0fS7nPj5ddYe+VVBvt7ZLPnufwDP4ieWcAWBWncR2lNkWb3TN6EMeePxEqZZ3N8gE+QdW+1HceDHTrzhXOcuXie9n6XuNvhzNkTqEBjHGihiOoV3GNPMJ3mdJ9/iVtrrzFz4TyPfHCJJElI4wRw5GmCEwIpNELC7vpN9rc2WDxzEaE1M/UGjThjc7/Pm6+/ibEO4Qytr/9zXPrQNyOMw8V9dnf2OXlypjRq5ARnH4xeDecx9BU5HEq9DWohTMQX3+rfxYRosZao2mTr5VdR0tGaaTEzO8+rL77K9tYujz/xbnSSsPxLH+Pm7Tdo/dlv4/SVJyhyH/zNs4Q8jcEZjLPUqgFxL6dSq7N48gw2j5k+dZ79V2+x+uXnuHVjnW4cc+ldj3D+I9/N1KXH2FvfQmqFKyw6qrCwuDA+fwQH/Cljrh6WwUiO6gcf0uFMeyEQSo8qRe754LKuHryxkCV99nb2mJpfYnp2mpXbt1CBYnp+Dic0A2NIrz5M61u+k1NnzhEiMKaP0orCFKzevEa/26femsMRsbm8TKPZIuun5P0urtdHba+QF5Y3Xn2N6cV53vtf/XVaFx6hs7lJp9MnSRL68cA7w0I94ekU957jRJzWQ330uObhgsg6QCs9TuSc2H4Ht+Jw8BIdBDz8rkdpt7sM+gOq1ZCoEhBqRaglO/0B0cOPcCZLWf5Xv4T8nr+MaDRQMiTf7bL5zEuox96JdoLGdItae8Bg84/I9ttoHHu3V7j5/JfI+ntkvS3e+Zf+Uzq5JCg6FCZneqZGmiS+pXUVgmDMMPcKJRyQ3UOXs4DDtM47MuBDcTHOuLqbzb3HzYwOozCqIrWmKArCSkC92iKOY7SW3HrjVeIkp9GaYq3dRn7g/aS3brF77XUufvjDZC+/SvzMs7z53LPMXzjFe//j72F3ZQ0dZJw5Mcvnf/PTPPv8l8n3e8zMVHjP936Umce/kSxNCbQiiJpYIwgDQRBW2FjdAFsMRzpqynCwk7+7az5SyLfr0HSjviJ3L8RYLko51FYEeZbR3t1mqlWnsJZBv0+Wpuxt7zI93eLEmTNUq1Xs4iJR7d10rr/OzHSdQR7D4hSnv/kDbC+vsLy2ivnEv8HEBd12G9pbXLu2TL+fMbs0T/CBb2LqXd9I3GszNT1NnlsGccbKzQ1qtRpZtkNYCWhMNbHGcKencGI2d8n2o6YqHxpwIXy7jkkrbBL7Mej+iBgWn/qoviOLU9I4odZqEtWbLJ06Q6PZJE0GFGmMdIZo6QSNc+cJFMway8Vv+rPsbq0RBQFF4Xj5818gffMVNm3OzCVB1O0x9fiTiLOPsr2+yfRUg7ifkqUFaeazfYs8Jk9ThCwTe77ioc+ESPS+lXEp5DEDLpVC63BiMHB3jY+YSHQXmCKn3+7Q298nqta4+PCjhFFEtd5g9fo1imxAtVIj7vZROkI66O/uEogCXamCUARBg9z5A6/SjJg6PUtlcYaVG2tcvnCRbi9mdkqx11N0Y8h7uzRbNdpbOwSBJityhBTsbO1Q5AVSSVzuDmSPTfrEJ2koUo7a8+pwIsVxV9+QO+XfOCbocwwrtTpFHlNtzHD18SfQWmMLR7+zz6Dfpt/tU2tUmVk8Rae9j81TlJaIoE5eOCpSkKcxz/3B73DlPU+wdPIUK90NqguLLJ5/BKkMc0snWVtZZelEne6gILr0EBtru8ydOM0gHrD55nUaMy0qYYUw9EVV48jVVyd7xHKTQwMuBL7P1UR62EHjwVtsk50ewqjCpUfeg3OC29feHBU7KQlRrUWjOUut1WRnfRVjfRgvTTMqlTq9nS1MNsCZjEsPv5PrX/wiUUOzdOlhTly8ShJnxPs79Dv7nH3oKoP2LqfOTVGpTjE91aDdHfgSR6XY3dpgaqrB9EyLojB/DBFxf64kOFIDkHtvvwm9dTJGaAxaCwa9AXmW0u/1iSoBU0tLKB3RaNVIkj6d7Q1Wbt2mWm/RbE6TpRn1SkB/fx+EYeH0WW49/wVmTj1Oc+4UzlrCUDPQIdWpGSq1OnFvQK+fUFjFqXMnUOubrK7usHRqiWZrhqge+UgVzt838RZADhlpqOLq+3AtwaG7umVZRqUS3qGvjgc4TGwfu3F9B7bFkycJwggVhGjp72CQQUgUhazeusHO+k1qoaBaDdlcvQU39lBhnXe890nyZECaGy68/0+Bk3S2N4AF8rxAkCNEwO7mJsZZwrCGrtTJ0gIlQ7JSZp89N4tU2nfBmAD7Tm3lzkuVho64Ywd86KXUWo9KMu5lGk8yjRAglcaZnNUbr1NpNH0+uRE+v9BY2vt7NKeaXLj6GKkN2d1aZ/b0SRSn2N9vM0gNral56q0pcmtIegm6GtGPC7SExdOXKYxk0E9B5FQqVayxBJUKeVZAnvPy62s0Z2d5z+MPEQQa8xXUwjt9RJNtPY4V8CH54tH8QEHpEOwx0H6A1hRIHdLt7JHF+9SmWkzPnSBLU0xhceT099vUmlM8/OQ3kaYxWr8PhG+fqrT0JePC56RPLZxFKoktO1EopcsmMoK5E4qiKNjbuE0QaNI4IapVOHX2FE4E7PcT1m5vwdd9dZ364M7lyEbPkQDP8xxnizsOzEkaq4XDVWnNnqbanKe7t0kn3KNSbbC+coOZuQUa01OE1WnyIkcIQVH4EnAhBEU+jJGW5SBCYLKCYaFPUXbdt2VQJE0SOt0+tVqd9t4+a6vLVKtVnnjyCvEgxsoQa4a2wlsbb5OKgHVHTwKCI3TIH4qUURHsXWaxmzD/PbdbmyOlo9KYwlro9zrMLZ2m2+lijPOdMIdcpSQyDEGpMp24BCQIfEy1UkGE5e+B9r1m/RehlaReDUkGXeLOFs1mk+eefYnl5RVkEKKEQY6eeRDEO0Xj6H3r7guHHxpw38nHjOT3vQ4ZMVGzKQSEUQ0d1gijGt2ddZRwJIM+3d1NAAa97thoSjPytXVsr4/Z7/rgtLXkWzvYzJD+0dPkt2/jspxibw/T63vQnb+ZqtMdsLW+QV6kLJ08yblzpwkrdfa21kiT4kDS0r3E4QHwndfBj+q4gqMEIKylyLPRoA+awRNpyxOqY701Tbe9S9xtU5+eJ4jqpHmHxuycvxLM5mAtsl6j8xu/wuDTnyK4cAlVqxM9+k701YfZ+6l/SDC/SHT+HO3/55cIrzxMtrqMnp5h9gd+BKTCGcvW2jLNRgXnaqTJgP7+Jpxcoru7zdLJM6Ps2EnRcXdxVal1MVHnc0T6Yz9hyATDhmKTbtiDNOlnKWOGQnoX6fQ0U7Pz9LsdBv0uzek51pdv09nd9ZVx1qEXFkBJXKAoTEb60nNgDPr0GWSzhjx/GX3uPHJ2Bn3iJCLuQ5kNq7Tm9ZdeYGNtlTTJefaZp5mZm0K6GOM0lXrzq8xxUr0dz+eo0R44ZLNf8DLcmjuykg6oUQerCoQAZ4zPVVEhab9H3N1hbnEJTM7+9ga1qTmElNjBgMq73gvpAHXqHPnOJtHSSUQYUf+Wb0NWqrg8p/Gt346ansFsbZa9rgJfKGUtl69cZXp2iuvX16g251g4eYo8iVk6fZpao+Vdx3cAPB773Rxkj1hjfwTAy0HKcRODewUgxodRWcZX/s2gu099apq016ZSCcvOnAaspdWs+VsByxLX2jd9Cy7PiS5dxRmDMwXRlUcmuuQDxqJn5gCBTVJkeZldpCz1qTmsvcUT7/kgm8srLC+v8/C7HvOH+VcIPBycixvdNfS2qoVBEI4cP+JA+bQ7YPiMuKd8zS0uoqMalahKt92h12kzs3CCy+98FyZPcUWBKwxCWGx73yf/l8A4IXD5sLZ+XNpps3SkoTjj5WSeZwhhMek+thgwPd2g12sw6O2h1EP3TK6/15W9o7JC89bJ+8cCOPjyQb/6B0/6O83joZyPqjW6+9vkRY9Gs0m3vY1QmixJGPT3kZUWul7FucpX9FV/NQpVyNUnPkR3b48b11c5cf4mp89c5NTZU1RqdYIwGtdvcjAue6+q5DuzzI5Ch79PE7j26pdZOnEape+9buPWRsNmXpAOEoq8oN6s43DEnX0AZH2Knd/7FI1nn8HVaox8McJfwlFenMkw40sIfMW+sz5NGgfWYLt9cuOY+pEfRTabdPbao1tfG82W91KawhftlojeKUbu1MWzLCdJUubmZo4M+KGzZ4UQhFGFoshGjqCDYE8mR/pmBUVRUK03UGrY3Q1ac6dxRYFq1BB5ysbP/xR6ZhaXFz75ffhcKUvTfkilI6lcbF8SLsAZxMIJouh/QFTqnDhZH2UE+poeN0o5HjmSv8KB6ctm7l9C55Hds7ZUR5xzoyrkiU8wlLfDoIQxuc/zLmWoKWzZMAaskuiZOVRryl+MZB3COZASl8QIrRFhUGbqlOXiOESgPajDUFij6cWAtWTGlBfkefi+mlS4lzPLWktwn+5GPpJi6fB3GAvEqIzw7kWxEzLwYA4iI5AmyBQ4Y7BFAaYAKbFZQvjII4ilRd+jqvC3SaE0otHA5YU/bI3BFf5F+RVylIDpX9Yafw/nW5jw91iBsi/WRAn4EehIHF6t1ChKZ9OdOpZ3Z/pumZN3KnjQx8WzXvso/8aW75X4uDgmePdjVL/1L3iVMLeoehMXhXR/8ieQD12l8b1/lfbf+VHfpKbsuzU+Be90THHPZgV3hwcPJnc6V9amwpHdV0fkcIspspFH8M5C0knn1uR7Iyt0DMW4/9X44QilcMKiH30X3Z/+ZySf/wxuuolNY5yxmGuvQb+LiCJ/kI6ce3c+/yAdKBv5KggOsw3uh5V5ZMCDIMIeEBniHirWOPrjOf5eMxwbRsI5XJ57uV4UyKhG7xf+BXTboBVmt0P/Z34Kl8aQ5cT/5uOQZR7kooByx03U506u4Sin/cDC3uGmPXitjOf4+xFegyOKlDCM6BqDmygDP2j8jGtkxi7bYULiwfTmUVVFGCIWFrD9GBXMkz/3RRCgTixilm/R/8WfQ7qC8LF3Y7a3SN98EVmv47TCSjVqv3T3d4zF16TNcK8Q4YFFKo3a+xHtOTLgAEWe3cUNb30IleDjLz66s0uakD6K0/zI9+CmZxGtJslvfJzpv/J9FCu3kecvYF58CXnlHdDrkX7u01Q+8GFyoUjTjLTfo1GRxB/7ecaHwfDh45KRt3In3wv4YUuS+0WH7yYBRFHVBxZMGX0p+/HcNZk7exeV/ZGGF1CPjjitkcKS/vovI6Karwdt79L56X+G63UR0zPYtWXk7Dym10VYg7t1A2sFrsjQeUYvjVGasqpOjBJOhwzhGHcdGg/nrSP3w+YHfyI4PIwqVOsNsjQmjGre5STFBMeUmoE9KDetMwgUd3oZnSkwSUy2fhuXev+IVJpsYxmk8t3GdUCxdguhFEIpkrWbZXMrgdQKIQV2et6fAUPtx7mxyHLcu3zbubt4wtsNhjAI7wvYcATTfkhpGrO5+ga1eosg9Lf5De9cG0a6x+ogB1RE8AFmr3dF2K0V0peeIY8LKD2IsjSKPGDGNwwLQr/Vrb/Z20lQYUTYqhO0mtigijr/DgjDModQllxaHnxuWPr41lwtSv27KArq9fp98aPcF8AB4kGH9s4K4AijOjqIkDocaSVjmXgwrcxaU2YLe01HqACi8dU0QkpMUSCEL6zyosub+9Ya7yK2FiEVSunSo+cFiUtihqlsQqryc+MCqrsq7UZeBC/rhykUURTdN3FynwD32oA1OZ29DZJBh7zIiCoNomoDHVR848jyo75Dg0UpDWUTRlsUpa4bgLMjV6goo/IjoCkb8A7zzodpGGWkZ7irhlcljIyvsou/Y5w1exB0UY5rfL2j1pogCO4bZ99HwA+SNQXd9g793h44gwoidBCidVjehqImTPyJuk5B2R5DjvzPk413D6hvUo2MG+vsKNY42eVzzNHDKjsQSL84Ez4xZ+0oSVMISRiEBGF434H+GgF+UPd1zpFnCUWRYYqcPM98L6w8RypFliYlV467y1prUToo2zyNlRsp7o4wGTOsYhDjYt0DpcLjwi4p/R3KSvm7laUaXoWj/J0+wbiw92tJ953Dh0DDWzuFfI6eI88ynLOkcb+0UwRp0scWRXmoDTNzvdubYQr0HRw/sk4oRTwQVWreEra+q0VUqY1ExWTC6XHT1wTweyzBBPO/PRP9k0JHv6/wP4jEV8T5ONb87eLoO+mYAP/K9CcFjOOgr/0p8YAO0APAj5keAH7M9ADwY6YHgB8zPQD8mOkB4MdMDwA/ZnoA+DHTA8CPmR4Afsz0APBjpgeAHzM9APyY6QHgx0wPAD9megD4MdMDwI+Z/j80Lz/YM2xOHgAAAABJRU5ErkJggg=="
img = readb64(data_uri)
cv2.imshow("img",img)
cv2.waitKey(0)