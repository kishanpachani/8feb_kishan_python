student = {
  'name': 'kajal',
  'class': '12',
  'roll_id': '2'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'kajal'})
print(student.keys() >= {'roll_id', 'name'})