let searchForm = document.getElementById('searchForm');
let pageLink = document.getElementsByClassName('page-link');

if (searchForm){
    console.log("pageLink : ");
    for(let i = 0;  pageLink.length > i; i++){
      pageLink[i].addEventListener('click', function (e) {
            e.preventDefault(); 
            // console.log("pageLink : ");
            let page = this.dataset.page;
            searchForm.innerHTML += `<input type="hidden"  name="page" value="${page}">`;
            searchForm.submit();
        })
    }
}   