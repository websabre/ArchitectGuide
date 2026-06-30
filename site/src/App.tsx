import { Routes, Route } from 'react-router-dom'
import { Layout } from './components/Layout'
import { HomePage } from './pages/HomePage'
import { DocPage } from './pages/DocPage'
import { AdminPage } from './pages/AdminPage'
import { AnalyticsTracker } from './components/AnalyticsTracker'

export default function App() {
  return (
    <>
      <AnalyticsTracker />
      <Routes>
        <Route path="/admin" element={<AdminPage />} />
        <Route element={<Layout />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/doc/*" element={<DocPage />} />
        </Route>
      </Routes>
    </>
  )
}
