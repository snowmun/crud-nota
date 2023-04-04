<template>
  <div id="content-wrapper" class="d-flex flex-column">
    <div id="content">
        <div class="container-fluid">
            <br/>
            <br/>
            <br/>
            <div class="text-center">
                <div class="error mx-auto" data-text="404">404</div>
                <p class="lead text-gray-800 mb-5">Page Not Found</p>
                <p class="text-gray-500 mb-0"> Parece que encontraste un error en la matrix...</p>
              <router-link to="/">&larr; Volver al Home </router-link> |

            </div>
        </div>
        
    </div>
    <footer class="sticky-footer bg-white">
      <div class="container my-auto">
          <div class="copyright text-center my-auto">
              <span>Copyright &copy; Orlando Muñoz 2022</span>
          </div>
      </div>
    </footer>
  </div>
</template>

<script>
import '@/assets/css/NotFoundPage.css';

  export default {
    name: 'NotFound',
    render: function (createElement) {
      return createElement('div', 'Not Found')
    }
  }
</script>