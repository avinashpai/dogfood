import React, {useEffect, useState} from 'react'
import './App.css'

const CarResults = () => {
  const [data, setData] = useState([{}])
  
  useEffect(() => {
   fetch("/members").then(
    res => res.json()
   ).then(
    data => {
      setData(data)
      console.log(data)
    }
   )
   }, [])
  
  const [carData, setCarData] = useState([{}])
 
  useEffect(() => {
    fetch("/cars").then(
      res => res.json()
    ).then(
      carData => {
        setCarData(carData)
        console.log(carData)
      }
    )
  }, [])

  return (
    (typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ): (
          data.members.map((member, i) => (
            <p key={i}>{member}
            <ul>
            {(typeof carData.cars === 'undefined') ? (
              <li>Loading Cars...</li>
            ): (
                (Object.keys(carData.cars).includes(member)) ? (
                carData.cars[member].map((car) => (
                  <li>{car}</li>
                ))
              ): (
                <li>None</li>
              )
            )}
            </ul>
            </p>
        ))
      ) 
  ) 
}

const App = () => {
   
  const [showCars, setShowCars] = useState(false)
  
  const onClick = () => setShowCars(true)

  return (
    <div>
      <input type="submit" value="Show Cars" onClick={onClick} />
      { showCars ? <CarResults /> : null }
          </div>
  )
}

export default App
