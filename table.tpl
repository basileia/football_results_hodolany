<!DOCTYPE html>
<html>
<style>
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    }
  th, td {
    padding: 5px;
    }
</style>
<body>
<table style="width:80%">
  <tr>
 {% for header in headers %}
 <th>{{ header }}</th>
 {% endfor %}
</tr>
 {% for result in results %}
   <tr>
 {% for i in range(result|length - 1) %}
 <td>{{ result[i] }}</td>
 {% endfor %}
 <td style="text-align:center">{{ result[-1] }}</td>
 </tr>
 {% endfor %}

</table>

</body>
</html>
