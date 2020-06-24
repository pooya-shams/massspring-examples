import massspring as ms
import massspring.networklib as nl

ms.acceleration.y = -ms.ge

m1 = ms.mass(moveable=False)
m2 = ms.mass(x=-100, y=-100)
s1 = ms.spring(m1, m2, k=100000)

kwargs = {"displaying": False}
nl.start_server_mainloop(ms, (), kwargs, nl.handle_client_wrapper(
    nl.analyse_request_wrapper(ms.mass_lis, ms.spring_lis)))
