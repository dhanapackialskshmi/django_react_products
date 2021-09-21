import React ,{useContext,useState} from 'react'
import { ProductContext } from '../Context/userContext'
import { useNavigate } from 'react-router';
export default function Product(props) {
    // const {name} = useContext(UserContext)
    // console.log(name)
    // const {products}=useContext(ProductContext)
    // const showProducts= products.map((products,index)=>{
    //   <li key={index}>{products}</li>
    // })
    // console.log(showProducts)
    const {products,setProducts} = useContext(ProductContext)
    const [Productname,setProductname]=useState('')
    const[description,setDescription]=useState('')
    console.log(products)

    const updateproductname=(e)=>{
      setProductname(e.target.value)

    }
    const updatedescription=(e)=>{
      setDescription(e.target.value)
    }
    
    const addProduct=(e)=>{
      e.preventDefault();
      //const navigate = useNavigate();


      console.log(Productname,description)
      setProducts(...products,{ Productname:Productname,description:description} )
    }
     return (
        <div className='col-lg-6'>
          <form className="form-inline" onSubmit={addProduct}>
            
              <div className="form-group">
                <label>Product Name</label>
                <input type="text" name="productname"id="product" value={Productname} onChange={updateproductname}></input>

              </div>
            
            
            
              <div className="form-group">
                <label>Product Description</label>
                <input type="text" name="productdescription"id="desc" value={description} onChange={updatedescription}></input>
                
            
            </div>
            <button type="submit" class="btn-btn-primary">Submit</button>
            </form>
            product {products.map(products=>
            <div key={products.base_id}>
            <h2>{products.productname}</h2>
            <h2>{products.description}</h2>
     </div>
            )}
          {/* show {showProducts} */}
          
        </div>
    )
}



