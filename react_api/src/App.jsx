
import React,{useState,useEffect} from 'react'
import Nav from './Components/Nav'
import {Product,List} from './Components'
import {UserProvider,ProductProvider} from './Context/userContext'
import {Home,Form,ProductPage} from './Pages/index'
import {BrowserRouter,Route,Routes} from 'react-router-dom'
// import Login from './Pages/Login'

function App(){
  
  
  return (
    <div className='App'>
    <h1>Welcome</h1>
    <ProductProvider>
     
      <Product />
    </ProductProvider> 
     <UserProvider>
      <List/>
    </UserProvider> 
    <Count/>
    {/* <Login /> */}

    <div className='container'>
      <BrowserRouter>
      <Nav />
      <Routes>
        <Route path='/' element={ <Product/>} />
        <Route path='/list' element={<List/>}/>
        {/* <Route path='/addProduct' element={ <AddProduct/>} />
        <Route path='/:id/' element={ <ProductDetail/>} />
        <Route  path="/:id/productDetail" element={ <ProductDetail/>}  />
        <Route path='/login' element={ <Login/>} /> */}
      </Routes>
     
      
      </BrowserRouter>
      
    </div>
    </div>
  )
}
 
export default App;
