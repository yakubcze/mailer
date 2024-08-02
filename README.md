Simple mailer daemon written in Python.

payRoll.py
- Retrieves events with certain name (ie. "WORK") from Google Calendar for previous month using Google API
- Creates HTML table containing work hours for every day of previous month
- Sends table via e-mail (using Google's SMTP server)


Example output: (for 100,- Kč/hour)
---
![image](https://github.com/user-attachments/assets/7faf76b9-ff4c-455e-bee0-8eef0473a6bd)
<table style="border-collapse: collapse;">
  <colgroup>
    <col style="width: 80px;">
    <col style="width: 80px;">
    <col style="width: 80px;">
  </colgroup>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;"><b>Datum</b></td>
    <td style="border: 1px solid black; text-align: center;"><b>Den</b></td>
    <td style="border: 1px solid black; text-align: center;"><b>Hodiny</b></td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;"></td>
    <td style="border: 1px solid black; text-align: center;"></td>
    <td style="border: 1px solid black; text-align: center;"></td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">01.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Ponděli</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">02.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Úterý</td>
    <td style="border: 1px solid black; text-align: center;">7.5</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">03.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Středa</td>
    <td style="border: 1px solid black; text-align: center;">7.5</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">04.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Čtvrtek</td>
    <td style="border: 1px solid black; text-align: center;">7.5</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">05.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Pátek</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black; background-color: green;">
    <td style="border: 1px solid black; text-align: center;">06.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Sobota</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black; background-color: green;">
    <td style="border: 1px solid black; text-align: center;">07.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Neděle</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">08.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Ponděli</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">09.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Úterý</td>
    <td style="border: 1px solid black; text-align: center;">7.75</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">10.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Středa</td>
    <td style="border: 1px solid black; text-align: center;">7.5</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">11.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Čtvrtek</td>
    <td style="border: 1px solid black; text-align: center;">4.0</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">12.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Pátek</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black; background-color: green;">
    <td style="border: 1px solid black; text-align: center;">13.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Sobota</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black; background-color: green;">
    <td style="border: 1px solid black; text-align: center;">14.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Neděle</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">15.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Ponděli</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">16.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Úterý</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">17.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Středa</td>
    <td style="border: 1px solid black; text-align: center;">7.5</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">18.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Čtvrtek</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">19.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Pátek</td>
    <td style="border: 1px solid black; text-align: center;">7.5</td>
  </tr>
  <tr style="border: 1px solid black; background-color: green;">
    <td style="border: 1px solid black; text-align: center;">20.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Sobota</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black; background-color: green;">
    <td style="border: 1px solid black; text-align: center;">21.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Neděle</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">22.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Ponděli</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">23.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Úterý</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">24.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Středa</td>
    <td style="border: 1px solid black; text-align: center;">7.5</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">25.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Čtvrtek</td>
    <td style="border: 1px solid black; text-align: center;">7.5</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">26.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Pátek</td>
    <td style="border: 1px solid black; text-align: center;">4.0</td>
  </tr>
  <tr style="border: 1px solid black; background-color: green;">
    <td style="border: 1px solid black; text-align: center;">27.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Sobota</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black; background-color: green;">
    <td style="border: 1px solid black; text-align: center;">28.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Neděle</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">29.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Ponděli</td>
    <td style="border: 1px solid black; text-align: center;">8.75</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">30.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Úterý</td>
    <td style="border: 1px solid black; text-align: center;">7.5</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">31.07.2024</td>
    <td style="border: 1px solid black; text-align: center;">Středa</td>
    <td style="border: 1px solid black; text-align: center;">-</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;"></td>
    <td style="border: 1px solid black; text-align: center;"></td>
    <td style="border: 1px solid black; text-align: center;"></td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">Celkem: </td>
    <td style="border: 1px solid black; text-align: center;">(h.)</td>
    <td style="border: 1px solid black; text-align: center;">92.0</td>
  </tr>
  <tr style="border: 1px solid black;">
    <td style="border: 1px solid black; text-align: center;">Výplata</td>
    <td style="border: 1px solid black; text-align: center;">(Kč,-)</td>
    <td style="border: 1px solid black; text-align: center;">9200.0</td>
  </tr>
</table>
