# Homelab

## Description

## Stack

## Write-up

### Hardware

As a tech enthusiast and Linux aficionado I love spending time exploring the
plethora of projects created by the greater open source community. I started
this journey by setting up a couple of basic services running as systemd units
on my desktop which was running Arch Linux at the time. The issue with this was
that I never had my desktop running 24/7 and the processing power of my gaming
CPU/GPU was not ideal for server scenarios. This eventually led me to purchase a
defunct Dell PowerEdge server from my university surplus and salvage store.
After a bit of refurbishing and struggling with decade-old BIOS, management
platform, and hardware RAID solutions I had the machine up and running.

### Software

At first, I used Proxmox as my hypervisor utilizing their built-in LXC container
support for deployment of my services. I eventually developed a distaste for the
freemium design of the service with its constant reminders that I was on a free
license and would not receive all of the security updates as often as I would if
I paid for their "pro" tier. It was around this time I made the switch from Arch
Linux to NixOS as my daily driver on my desktop and was having a blast with
Nixlang and the declarative, atomic structure of this OS as well as the promises
and peace of mind that come with it. After a little research into Nix flakes and
modules, I dove into re-writing all of my container startup scripts as NixOS
modules relying on this built-in oci-container support to declare and run my
docker-compose instances as integral systemd services. This allowed me all of
the benefits of NixOS with little to no transitional friction aside from
translating my compose files to Nixlang-compatible definitions. As time has gone
on and I have run into more and more issues dealing with dockers monolithic
daemon I have begun to re-write some of these services as base nix modules (yay
flakes) with the services running bare-metal while still using quarantined file
volumes and firewalls to preserve the security up-sides of containerized
deployment. The one issue I have run into with this approach is when you
encounter a service that is not already packaged and maintained in the base
nixpkgs repo. Thanks to my experience with Linux package managers from my time
on Arch using the AUR I was able to get up to speed with packaging for NixOS
with a little bit of reading the man pages. I have now been able to package all
of the services I would need utilizing Nixlang's derivations. I currently have
open pull requests to the nixpkgs repo for some of the software I have packaged.

### Networking

Around the time I was still running Proxmox, I was taking a networks class at
uni and became infatuated with the DNS hierarchy and design. I decided to
purchase my first domain name as well as set up Cloudflare as my DNS provider. I
spent quite a bit of time setting up my DNS records to allow myself as well as
my colleagues to access the services I was hosting in a way that was both
dependable and secure (shout out to Cloudflares free per-record DNS proxies).
Somewhere along this journey, I made the realization that my IPS-issued router
with its garbage firmware was not cut out for the type of environment I was
deploying it in. As a college student strapped for cash I could not shell out
the insane premium required for professional-grade equipment and once again had
to turn to the surplus and salvage to buy a cheap desktop that had been retired
from the library to deploy OPNsense. This gave me the flexibility and freedom to
set up my networking environment, DNS servers, blocklists, firewalls, etc
exactly as I saw fit without faffing about with the child locks baked into
ISP-designed firmware. This all worked great until I recently graduated and had
to move. I ended up living in an area with only one ISP with fiber service, the
worst part was that this ISP was CG-NATed. This meant that I could no longer
make my services accessible simply by port-forward. I reached out to the ISP to
request a static public IP allocation and was ignored. I decided I would have to
take matters into my own hands after some research I landed on a multi-faceted
solution to my problem. I deployed Tailscale's free personal VPN service to
access my machines and various admin management dashboards securely and once
again turned to Cloudflare for my services that necessitated public access.
Cloudflare offers free TCP tunnels via their cloudflared daemon. Once I had that
set-up I was able to simply generate CNAME records that pointed to the exposed
tunnel hooks for seamless integration. However, despite Cloudflare's claims that
their tunnels support all TCP traffic, it would appear that it required the
traffic to support HTTP-terminated packets, which most game servers do not. I
had to turn to playit.gg and their tunnels to open access to the various game
servers I host. After some SRV record wizardry to redirect my hostnames to the
dynamically allocated playit.gg tunnels public IP/port combos all was running as
expected.

## Links

[Nix Config](https://github.com/Guno327/nixcfg/tree/main/hosts/nixos-server)\
[Custom Pkgs](https://github.com/Guno327/pkgs)
