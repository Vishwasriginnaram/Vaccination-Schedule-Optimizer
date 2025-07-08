document.getElementById('form').addEventListener('submit', async function(e) {
  e.preventDefault();

  const age = parseInt(document.getElementById('age').value);
  const conditions = document.getElementById('conditions').value.split(',');
  const region = document.getElementById('region').value;

  const response = await fetch('http://localhost:5000/generate_schedule', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ age, conditions, region })
  });

  const data = await response.json();
  document.getElementById('result').textContent = JSON.stringify(data, null, 2);
});
