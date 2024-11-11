// * React Libraries
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { Provider } from 'react-redux'

// * Components
import { AppWrapper } from './AppWrapper.tsx'

// * Store
import { store } from '@store'

// * Styles
import './index.scss'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Provider store={store}>
      <AppWrapper />
    </Provider>
  </StrictMode>,
)
