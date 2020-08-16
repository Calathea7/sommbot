document.querySelector('#wine-search').addEventListener('submit', (evt) => {
  evt.preventDefault();

  const formInputs = $('#wine-search').serialize();
  // const year = document.querySelector('#year').value;
  // const minPrice = document.querySelector('#min-price').value;
  // const maxPrice = document.querySelector('#max-price').value;
  // const descriptors = document.querySelectorALL('.descriptor').value;

  $.post('/recommendation', formInputs, (res) => {
    alert(res);
  });

});
