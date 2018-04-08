var form = document.getElementById("form");
var roster = { "Six": ["Abdullahnayeem","Angela","Anish","Bayan","Blythe","Brian","Charlotte","Datian","David","Emily","Irene","Jenny","Jonathan","Kaia","Kenneth","Kent","Lorenzo","Lydia","Matthew","Max","Maya","Mohamed T","Mohammad N","Nusheen","Oskar","Sarah","Rachel","Sakib","Shaikh","Sienna","Taylor","Yiduo","Yousuf","Zachary"], "Eight": ["Andre","Calvin","Cynthia","Daniel","David","Eli","Eric","Garrett","Gilvir","Ginevra","Isaac","Jacopo","Justin","Kai Hei","Kelly","Kevin","Leila","Megan","Michelle","Mika","Minseo","Nicholas","Pacy","Rochelle","Sammi","Sarah","Pallab","Simon","Sofiya","Stefan","Stephanie","Tahseen","Tiffany","Vicky"] };
var num = 0;
var create_student_td = function(student) {
  var td = document.createElement("td");
  var checkbox = document.createElement("input");
  checkbox.setAttribute("type", "checkbox");
  checkbox.setAttribute("name", student);
  checkbox.setAttribute("id", "s" + num);
  td.appendChild(checkbox);
  var label = document.createElement("label");
  label.setAttribute("for", "s" + num++);
  label.innerHTML = student;
  td.appendChild(label);
  return td;
};
var create_table = function(students, id, visible) {
  var table = document.createElement("table");
  table.setAttribute("id", id);
  if (!visible) table.style = "display:none";
  var row = document.createElement("tr");
  var i;
  for (i=0; i<students.length; i++) {
    if ( i%7 == 0 && i>1) {
      table.appendChild(row);
      row = document.createElement("tr");
    }
    row.appendChild(create_student_td(students[i]));
  }
  table.appendChild(row);
  return table;
};
form.appendChild(create_table(roster["Six"], "period6", true));
form.appendChild(create_table(roster["Eight"], "period8", false));
var submit = document.createElement("input");
submit.setAttribute("type", "submit");
form.appendChild(submit);
var period6 = document.getElementById("period6");
var period8 = document.getElementById("period8");
document.getElementById("6").addEventListener("click", function() {
  period6.style = null;
  period8.style = "display:none";
});
document.getElementById("8").addEventListener("click", function() {
  period6.style = "display:none";
  period8.style = null;
});
