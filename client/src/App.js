import React, {useEffect, useState} from 'react'
import './App.css'

function App() {
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
    <div>
      {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ): (
          data.members.map((member, i) => (
            <p key={i}>{member}
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
            </p>
        ))
      )}
    </div>
  )
}

export default App
