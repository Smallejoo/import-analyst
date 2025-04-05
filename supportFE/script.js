document.addEventListener('DOMContentLoaded', () => {
    // Make the month amount span update when a label is clicked



    document.querySelectorAll('.clickble-option').forEach(label => {
      label.addEventListener('click', () => {
        const value = label.innerText.trim();
        document.querySelector('#sarch-amount-span').innerText = value + " rows";
    
        fetch('/api/data?amount=${value}')  // ✅ fixed with backticks
          .then(res => res.json())          // ✅ fixed with ()
          .then(data => {
            console.log("Received:", data);
    
            const tableBody = document.getElementById('tableBody');
            tableBody.innerHTML = '';
    
            data.forEach(row => {
              const tr = document.createElement('tr');
              tr.innerHTML = `
                <td>${row.Year || ''}</td>
                <td>${row.Origin_Country || ''}</td>
                <td>${row.CustomsItem_8_Digits || ''}</td>
                <td>${row.NISCurrencyAmount || ''}</td>
                <td>${row.Month || ''}</td>
                <td>${row.Quantity || ''}</td>
                <td>${row.Quantity_MeasurementUnitName || ''}</td>
                <td>${row.TradeAgreementName || ''}</td>
                <td>${row.CustomsHouse|| ''}</td>
                <td>${row.VAT || ''}</td>
              `;
              tableBody.appendChild(tr);
            });
          });
      });
    });
  
    // Optional: column visibility toggle logic
    document.querySelectorAll('.column_toggle').forEach(checkbox => {
      checkbox.addEventListener('change', function () {
        const colIndex = this.getAttribute("data-col");
        const isChecked = this.checked;
  
        document.querySelectorAll('table tr').forEach(row => {
          const cell = row.children[colIndex];
          if (cell) {
            if(isChecked === true)
            {
                cell.style.display ='';
            }
            else{
                cell.style.display ='none';
            }
          }
        });
      });
    });
  });
  