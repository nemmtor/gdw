# -*- coding: utf-8 -*-
from config import klient, konsultant


def stworz_subject(subject_type):
    if subject_type == 1:
        subject = "Umowa_" + klient.imnaz + "_" +\
            klient.datasprz + "_" + klient.cena_dl
    return(subject)

def stworz_rodo():
    with open("pliki/rodo.txt", "rb") as f:
        tresc_rodo = f.read().decode("UTF-8")
    body = tresc_rodo
    f.close()

    body += '<br>' * 2

    body += 'Pozdrawiam,<br>'

    body += '<i>{}</i>'.format(konsultant.kto)

    body += '<p style="font-size:10px;">{}</p>'.format(konsultant.login)

    body += '''<hr align="left";
                   width="25%";
                   style="height:0.1px;
                   background-color:gray;" >'''

    body += '<br>'

    # body += '''<img src="data:image/jpeg;base64,/9j/4QAYRXhpZgAASUkqAAgAAAAAAAAAAAAAAP/sABFEdWNreQABAAQAAABkAAD/4QRfaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjMtYzAxMSA2Ni4xNDU2NjEsIDIwMTIvMDIvMDYtMTQ6NTY6MjcgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcFJpZ2h0cz0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3JpZ2h0cy8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtcFJpZ2h0czpNYXJrZWQ9IlRydWUiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpkZmFkYmFjMC0wM2E0LTA1NGItODIwZi05ZDA2MzliNzZlNzMiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MDhCQThGMEE1N0JBMTFFNTk4OTVCMTc1MkREMDU2NTciIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MDhCQThGMDk1N0JBMTFFNTk4OTVCMTc1MkREMDU2NTciIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo4MEM3NzYyQkM3NEJFNTExQTEwMUIwQkU4NjlFRTk3RSIgc3RSZWY6ZG9jdW1lbnRJRD0iYWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOmExNTMxMDI5LWIyYzQtMTFlNC1hNjdiLWIxMDdhM2ViNWRkNyIvPiA8ZGM6Y3JlYXRvcj4gPHJkZjpTZXE+IDxyZGY6bGk+SW5zcGVjdCBCcmFuZCAmYW1wOyBXZWIgRGVzaWduPC9yZGY6bGk+IDwvcmRmOlNlcT4gPC9kYzpjcmVhdG9yPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Pv/tAEhQaG90b3Nob3AgMy4wADhCSU0EBAAAAAAADxwBWgADGyVHHAIAAAIAAgA4QklNBCUAAAAAABD84R+JyLfJeC80YjQHWHfr/+4AJkFkb2JlAGTAAAAAAQMAFQQDBgoNAAAHzQAACfEAAAumAAANpf/bAIQAAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQICAgICAgICAgICAwMDAwMDAwMDAwEBAQEBAQECAQECAgIBAgIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMD/8IAEQgAKAAhAwERAAIRAQMRAf/EAN8AAAICAwEAAAAAAAAAAAAAAAcIBAYAAgkFAQACAQUBAAAAAAAAAAAAAAAFBgcAAQIDBAgQAAEEAgEEAwAAAAAAAAAAAAQAAgMFAQYTEBIUFREWFxEAAQMCAgcFBAsBAAAAAAAAAwECBBESABMQIVFhIhQFMUFxcoKBoVKTMmKyIzNTYzTUFTUGEgABAgIFCgMJAAAAAAAAAAABAAIRAxAxQVEyIWFxgaGxweESItETM/CR8UJSstIEFBMBAAEDAwMEAwEAAAAAAAAAAREAITEQQVFhcYGRocHxsdHh8P/aAAwDAQACEQMRAAAB7DpJ4Lp5w+vS9te1dH9KmRa3x9eRTZhRqcQaTw48lppDiVWMStmHTv0jFlZHdS7oDItEdNGVT2zagGlwCUwP2plELt5fNtdCX0kiMA3/2gAIAQEAAQUC/Q6Ds3HY5bNaVbutKczdKmvI/R6RVAPsrKyK80/QrHw7reqD2Aa1uPgDUEzx5hCGGC/W6JWte+h0/poZvlUCvKQW+EuNOuKlVOsW9xnXddg14df/2gAIAQIAAQUC98D8W1g4lU5WSRJbgWCT7AGhYfIIIk5p6MjiMugeeJV7eyJMdmN8UmJYvXhIqDIVT0o5uQFGhxmxF1JYqFrSi1XgMAjX/9oACAEDAAEFAvXEfIQ2IkdDxTMCmkb62dTP44o29kdhH3wAEcb0Tnues4w7D25Y7yZ1FJggzpYM7SFBO6B8JkMymKhhRJOSHL//2gAIAQICBj8Cj3x0c0yW2LWQjDTVHVl1qD/UZkPBGVNDxMGZYZnuH5JkmwnZbsTplhOyxeWcMwQ12eGtf0y/VZtHKif+19EuA0uyUB7cQMU2aMLhFem1GW7E+d8PtjSG2sMONHlTIi5Rh1yrxxC7Gwl3mrmi0Elzq6P/2gAIAQMCBj8C+VFxyujBZMLkHs6ekqtu3wRfcEG5l1WtXlOwHfRLk3u3UdJqKLTWCsRQcKms9t9MbHUdTVCp+ddx7rlEiAFH/9oACAEBAQY/ArrZ935fLsv8K5+X78Qo4mliAyWyyBUnG5T8UVTW8NeWteia6ZmGtM9XyoL+WK5y1e9lLgEd3rUfDXvVq4PEmCnBkR3WuHkNdd3teNyFtcMjVq1dWpcfteqfJi/zMQ4XY05moVfhA37w7/QFqriXKRKNMd7ht7mBRbQjRNgxIiezCRnOoLqI1AuzPZUgF8aorU8+P7OMysyCxc1GprPESrnJveD6Sbq7tH/QdXXVyXS3xgu+GT1Bcgbm72p9rQGQJaEAVhhrseNyPavsVMR5Q/w5IBHb5SsR9F8K4/yofysHilS00/rbkfvEJ5FD6HDho9PNpGJVq+CYsZdtlc4S+FpbU8ujlZLiDsfmhKJdYy2q261eF7aO1ovuw5+VzsRNfMxWq6jf1g6yC39rd+EWPHUUde2XIqIFPqqqXF9CLggxmJINIVjpBHcLFcNHI1BC15bUu2qq6P/aAAgBAQMBPyHoYnfvUKj501viYgAZAyUtvf1IszKNJXWaepV+MFORMZBINtACS0CLF7K29HUEAZZHCUF5xS3s6WDI/K6mp4RCSiLpXkZu6IiXH2uxcdNH8OGT5OrvwzmB3UEXrX0j91HJNbo0TPys65r1zkHadMCXVhJhqZzAMNlXpA3NEDtxlBlB86f7FiTcsucXOYq0dlvAFAHncmwFf//aAAgBAgMBPyHaulCfh71HG75XcrXaChpJbrJu9LdUaZUsJD1GcJc6aau+j6C68BqE7Lg42PBBVyPxC/yot7av/nOR0nppM+76WfHzpZiEO4yVgxI8k19fVna+7C+hAO+sk5vjh7MeNJcwMo2cYw/7FSnrH8h7nWmh8ReG/gNQg2U2LcG2erp//9oACAEDAwE/IcTDmf5ViuY7ZjzbxQSmCk+T/c0oC3J/m1fc0ct2O+3vXPZd3396snNPjD+/FXBu26f1j007wb2v0c4CPWshQPSvv6/eVWJ+HjWWOAfh/GlrbJCO5WcdL4OH89KFiTgu/wA80GBhH7dP/9oADAMBAAIRAxEAABDqUn5BDGYCjpof/9oACAEBAwE/EBAjupIhNi4bTb1qH+LiqgcErGQKMHY/FC+jEV1SzUKpvdktxIjkkKzsdSukJVog6oTmZo30pRJ4dbiKwdZkENszX9yo6a2cdgDlH4SCkiIDLmaxLmGATk0SCZcyH8I3TJiiMFpTFfQxYlgiaajOWwF34eEkAsJNbZxmZvw6sYhG2hXxlLr1WGi1sMzaJtixA3N0YKgktJp0Y4ZY7GLhXQ3JN69NSox6P//aAAgBAgMBPxA40fGTSAiIdcYiybEUN6lkrz4swJfdm6t0m7V+bM07goqhFJRIMhVBsYAf2EHijJSjaBgehh0Ki4zHxcfuoHWmYK4hcZU63eZG7DRrQkHCQOok8edHnlTwJPCFexi4QHtMOnx/lTku/wCAO7rJmVXMmXsQv00HoJ7vGhVYhRHZsq9IiwvAwObnXbPOl7M3ni6k8F5mM0kZrmEoF+BLKm7ABX//2gAIAQMDAT8Q3XuMfL2pV0wAWC29fe207YpMaEiwOC7N4wAKNm0kpHIjIVIl7llzp456kOXY+UFTjcwucl3Ur3qaGe6ys/hUx4vjjEeLV1lYnSBrxlzej0WPTQ3ZajkEPs1leR3SfGjGLkidj1BS1QYjyX8kye+kOrAFpBicjJZPIlqGFO3gl+gLUJBnw+W8eQ6TQfAQrsMTyNjYDYytf//Z">'''

    body += '<p style="font-size:9px;">Grupa Prawna Goldwin S.A.</p>'

    body += '<p style="font-size:9px;">Ul. Kościuszki 71/304</p>'

    body += '<p style="font-size:9px;">87-100 Toruń</p>'

    body += '''<p style="font-size:9px;">
               <span style="color:#d49b48">T:</span> +48 222 692 222</p>'''

    body += '''<p style="font-size:9px;">
               <a href="www.gpgoldwin.pl"
                style="color:#d49b48; text-decoration: none;
                border-bottom:0.5px solid blue">
                www.gpgoldwin.pl
                </a></p>'''

    body += '<br>'

    body += '''<p style="font-size:9px;">
               KRS: 0000586888 NIP: 8792679200, REGON: 362044066
               </p>'''

    body += '''<p style="font-size:9px;">
               Oznaczenie sądu rejestrowego: Sąd Rejonowy w Toruniu,
               </p>'''

    body += '''<p style="font-size:9px;">
               VII Wydział Gospodarczy Krajowego Rejestru Sądowego,
               </p>'''

    body += '''<p style="font-size:9px;">
               kapitał zakładowy: 150.000,00 zł w całości wpłacony
               </p>'''

    body += '<br>'
    # body += '''<img src="data:image/jpeg;base64,/9j/4QAYRXhpZgAASUkqAAgAAAAAAAAAAAAAAP/sABFEdWNreQABAAQAAABkAAD/4QRfaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjMtYzAxMSA2Ni4xNDU2NjEsIDIwMTIvMDIvMDYtMTQ6NTY6MjcgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcFJpZ2h0cz0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3JpZ2h0cy8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtcFJpZ2h0czpNYXJrZWQ9IlRydWUiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpkZmFkYmFjMC0wM2E0LTA1NGItODIwZi05ZDA2MzliNzZlNzMiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MDhDMEY3QkY1N0JBMTFFNTk4OTVCMTc1MkREMDU2NTciIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MDhDMEY3QkU1N0JBMTFFNTk4OTVCMTc1MkREMDU2NTciIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo4MEM3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">'''

    body += '''<p style="font-size:9px; color:#7d7d7d">
    Wiadomość ta jest poufna i zastrzeżona.
    Zabronione jest przeglądanie, przekazywanie, rozpowszechnianie lub
    inne wykorzystywanie tych informacji, jak również podejmowanie działań
    na ich podstawie przez osoby lub podmioty inne niż zamierzony adresat.
    <br>Jeżeli otrzymali ją Państwo omyłkowo, prosimy poinformować o tym
    Nadawcę i usunąć z komputera wiadomość wraz z załącznikami.</p></body></html>'''

    return(body)




def stworz_body():
    if konsultant.wybor == 1:
        body = '''<html><body style=font-family:"Arial","sans-serif">
        <p>Imie i nazwisko: {} </p>'''.format(klient.imnaz)
        body += '<p>Nr telefonu: {} </p>'.format(klient.tel)
        body += '<p>Data doręczenia: {} </p>'.format(klient.datawys)
        body += '<p>Adres email: {} </p>'.format(klient.mail)
        if not klient.rej_var:
            body += '<p>Adres rejestrowy: {} </p>'.format(klient.rej)
        if not klient.kor_var:
            body += '<p>Adres korespondencyjny: {} </p>'.format(klient.kor)
        if not klient.dost_var:
            body += '<p>Adres dostarczenia: {} </p>'.format(klient.dost)
        body += '<p>Branża: {} </p>'.format(klient.branza)
        body += '<p>Pytania do prawnika: {} </p>'.format(klient.pytania)
        body += '<p>Dodatkowe informacje: {} </p>'.format(klient.dodatkowe)
        body += '<br>' * 2
        body += 'Pozdrawiam,<br>'
        body += '<i>{}</i>'.format(konsultant.kto)
        body += '<p style="font-size:10px;">{}</p>'.format(konsultant.login)
        body += '''<hr align="left";
                       width="25%";
                       style="height:0.1px;
                       background-color:gray;" >'''
        body += '<br>'
        # body += '''<img src="data:image/jpeg;base64,/9j/4QAYRXhpZgAASUkqAAgAAAAAAAAAAAAAAP/sABFEdWNreQABAAQAAABkAAD/4QRfaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjMtYzAxMSA2Ni4xNDU2NjEsIDIwMTIvMDIvMDYtMTQ6NTY6MjcgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcFJpZ2h0cz0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3JpZ2h0cy8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtcFJpZ2h0czpNYXJrZWQ9IlRydWUiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpkZmFkYmFjMC0wM2E0LTA1NGItODIwZi05ZDA2MzliNzZlNzMiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MDhCQThGMEE1N0JBMTFFNTk4OTVCMTc1MkREMDU2NTciIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MDhCQThGMDk1N0JBMTFFNTk4OTVCMTc1MkREMDU2NTciIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo4MEM3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">'''
        body += '<p style="font-size:9px;">Grupa Prawna Goldwin S.A.</p>'
        body += '<p style="font-size:9px;">Ul. Kościuszki 71/304</p>'
        body += '<p style="font-size:9px;">87-100 Toruń</p>'
        body += '''<p style="font-size:9px;">
                   <span style="color:#d49b48">T:</span> +48 222 692 222</p>'''
        body += '''<p style="font-size:9px;">
                   <a href="www.gpgoldwin.pl"
                    style="color:#d49b48; text-decoration: none;
                    border-bottom:0.5px solid blue">
                    www.gpgoldwin.pl
                    </a></p>'''
        body += '<br>'
        body += '''<p style="font-size:9px;">
                   KRS: 0000586888 NIP: 8792679200, REGON: 362044066
                   </p>'''
        body += '''<p style="font-size:9px;">
                   Oznaczenie sądu rejestrowego: Sąd Rejonowy w Toruniu,
                   </p>'''
        body += '''<p style="font-size:9px;">
                   VII Wydział Gospodarczy Krajowego Rejestru Sądowego,
                   </p>'''
        body += '''<p style="font-size:9px;">
                   kapitał zakładowy: 150.000,00 zł w całości wpłacony
                   </p>'''
        body += '<br>'
        # body += '''<img src="data:image/jpeg;base64,/9j/4QAYRXhpZgAASUkqAAgAAAAAAAAAAAAAAP/sABFEdWNreQABAAQAAABkAAD/4QRfaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjMtYzAxMSA2Ni4xNDU2NjEsIDIwMTIvMDIvMDYtMTQ6NTY6MjcgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcFJpZ2h0cz0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3JpZ2h0cy8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtcFJpZ2h0czpNYXJrZWQ9IlRydWUiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpkZmFkYmFjMC0wM2E0LTA1NGItODIwZi05ZDA2MzliNzZlNzMiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MDhDMEY3QkY1N0JBMTFFNTk4OTVCMTc1MkREMDU2NTciIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MDhDMEY3QkU1N0JBMTFFNTk4OTVCMTc1MkREMDU2NTciIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo4MEM3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">'''
        body += '''<p style="font-size:9px; color:#7d7d7d">
        Wiadomość ta jest poufna i zastrzeżona.
        Zabronione jest przeglądanie, przekazywanie, rozpowszechnianie lub
        inne wykorzystywanie tych informacji, jak również podejmowanie działań
        na ich podstawie przez osoby lub podmioty inne niż zamierzony adresat.
        <br>Jeżeli otrzymali ją Państwo omyłkowo, prosimy poinformować o tym
        Nadawcę i usunąć z komputera wiadomość wraz z załącznikami.</p></body></html>'''
    return(body)
