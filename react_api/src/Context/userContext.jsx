import React,{createContext,useEffect,useState} from 'react';
import {useNavigate} from 'react-router-dom';
import axios from 'axios';

export const UserContext = createContext();
export const ProductContext=createContext();

export function UserProvider(props){
  
  const[name,setName]=useState([])
 useEffect(()=>{
      setName(['Dhanam','Dhanam123'])
  },[])

  return(
    <div className='user'>
      <UserContext.Provider value= {{name}} >
      hiii {props.children}
      
      </UserContext.Provider>
    </div>
      
  )
}

// const getProducts = async()=>

// {
//    const response =await axios.get("http://127.0.0.1:8000/api_json/base/")
//    setProducts(response.data)
//    console.log(response.data)
// }
// useEffect(()=>{
//   getProducts
// },[])
export function ProductProvider(props)
{
const[products,setProducts]=useState([])
const getProducts =async()=>
{
  const response =await axios.get("http://127.0.0.1:8000/api/base/")
  setProducts(response.data)
  navigate('/')

  console.log(response.data)
}
useEffect(()=>{
  getProducts();
},[])

return(
  
  <ProductContext.Provider value={{products,setProducts}}>
    {
    props.children
    }
  </ProductContext.Provider>
  
)
}