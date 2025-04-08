document.addEventListener('DOMContentLoaded', () => {
  //if you want to sort any colmn with a click 
  document.querySelectorAll("th").forEach((header, colIndex) => {
    header.addEventListener("click", () => {
      const rows = Array.from(document.querySelectorAll("#tableBody tr"));
  
      rows.sort((a, b) => {
        const cellA = a.children[colIndex].innerText.trim();
        const cellB = b.children[colIndex].innerText.trim();
  
        let valA, valB;
  
        if (isNaN(cellA)) {
          valA = cellA;
        } else {
          valA = parseFloat(cellA);
        }
  
        if (isNaN(cellB)) {
          valB = cellB;
        } else {
          valB = parseFloat(cellB);
        }
  
        if (valA < valB) {
          return 1;
        } else if (valA > valB) {
          return -1;
        } else {
          return 0;
        }
      });
  
      const tbody = document.querySelector("#tableBody");
      rows.forEach(row => {
        tbody.appendChild(row);
      });
    });
  });
  

// the function will try to show only the data that you sarch for by word 
// if the word is in any row the row will stay.
  document.querySelector("#overAllSearchBar").addEventListener('click', () => {
    const searchName = document.querySelector("#sarchBar").value.toLowerCase();
  
    document.querySelectorAll("#tableBody tr").forEach(row => {
      const rowText = row.innerHTML.toLowerCase();
  
     
      row.style.display = "none";
  
     
      if (rowText.includes(searchName)) {
        row.style.display = "";
      }
    });
  });
  

  const graphs=document.querySelector(".graphs-div")
//the button for the graphs when you finish adjusting witch graph you want 
// you will click on this button and the graph will soon be on the window . 
document.querySelectorAll(".Gbuttons").forEach(button =>
{
  button.addEventListener('click', ()=>
  {
   const closeParent=  button.closest(".graph-block")
   const spans=closeParent.querySelectorAll(".click-span")
   console.log(spans);
   const value1=spans[0].innerHTML;
   const value2=spans[1].innerText;
   const value3=spans[2].innerText;
   console.log(value1);
   console.log(value2);
   console.log(value3);
   const amount=document.querySelector("#sarch-amount-span").getAttribute("rows-amount-storage");
   fetch('/api/graph',{
    method:'POST',
    headers:{
      'Content-Type':'application/json'
    },
    body: JSON.stringify({
      graphType:value1,
      item1:value2,
      item2:value3,
      item3:amount
    })
   })
   .then(res=> res.blob())
   .then(blob => {
    const url=URL.createObjectURL(blob);
    if(closeParent.id==="graph-1")
    {
      document.querySelector("#GL1").src=url;
      console.log("iam here 1")
    }
    else{
      document.querySelector("#GL2").src=url;
      console.log("iam here 2")
    }
    console.log(url);

   })
  });
});


//shows what you have clicked so you will be sure what you have picked .
  graphs.querySelectorAll(".graph-block .clickble-option").forEach(label =>
  {
    label.addEventListener("click", ()=>{
      const closeParent = label.closest(".column-dropdown").querySelector("span");
     closeParent.innerText=label.innerHTML;

    });
  });
  
    //fetch command to the back end how much rows you want . 
    document.querySelectorAll('#drop-row-amount .clickble-option').forEach(label => {
      label.addEventListener('click', () => {
        const value = label.innerText.trim();
        const item=document.querySelector('#sarch-amount-span');
        item.innerText=value +" rows";
        item.setAttribute("rows-amount-storage",value);
        console.log(value);
        fetch(`/api/data?amount=${value}`)  // ✅ fixed with backticks
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
    document.querySelectorAll('#sarch-amount-span-bott-1 .clickble-option, #sarch-amount-span-bott-2 .clickble-option ').forEach(label=>{
      label.addEventListener('click', ()=>
      {
       const amount=document.querySelector("#sarch-amount-span").getAttribute("rows-amount-storage");

      })
    })
  
    //if you want to disable a column (toggle view )
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
  