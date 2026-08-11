# DNS Amplification Attack

A DNS Amplification Attack is a **Distributed Denial of Service (DDoS)** tactic that belongs to the class of reflection attacks. In this attack, an attacker delivers traffic to the victim by reflecting it off a third party (DNS servers), concealing the true origin of the attack.

The attack combines **reflection** with **amplification**: the byte count of traffic received by the victim is substantially greater than the byte count of traffic sent by the attacker, effectively multiplying the attacker's sending power.

## How the Attack Works

#### Core Attack Mechanics

A DNS Amplification Attack exploits three key characteristics of basic DNS protocols:

1. **UDP Transport**: UDP makes it substantially easier for attackers to spoof source addresses compared to TCP-based protocols.

2. **Open Recursive Resolvers**: Unrestricted or "open" recursive resolvers exist in large numbers on the internet and can be abused by attackers to reflect traffic.

3. **Response Amplification**: A DNS reply can be many times larger than the DNS query that generated it. By sending a small query known to produce a large answer, attackers achieve amplification.

#### Attack Flow

1. **Reconnaissance**: The attacker identifies a large set of open recursive resolvers to use as reflectors.

2. **Spoofing**: The attacker sends UDP DNS queries (typically of type `ANY`, `TXT`, or DNSSEC record queries that produce large responses) to the reflecting resolvers, with the source IP addresses spoofed to appear as the victim's IP address.

3. **Amplification**: The reflecting servers process the recursive queries and send responses to the spoofed source IP—the victim.

4. **Bombardment**: From the victim's perspective, the effect is a bombardment of unrequested DNS query responses from a huge multitude of nameservers.

#### Amplification Potential

- The amplification factor is calculated as the ratio between the response size and the request size, with factors **up to 4,670x** possible.

- A small 64-byte query can generate responses of several kilobytes.

- The classic Spamhaus attack in March 2013 was cited as a primary example of this tactic.



## Real-World Examples

#### The 2013 Spamhaus Attack

In March 2013, The Spamhaus Project was targeted by a massive DDoS launched in retaliation for their decision to list European ISP CyberBunker as a source of spam. DNS Amplification was cited as the primary tactic exploited by the attackers.

#### 

#### The 2016 Dyn Attack

On October 2, 2016, a huge attack was conducted against the servers of Dyn, a company that controls many Internet DNS servers. As a consequence, many popular Internet services (Amazon, Twitter, GitHub, PayPal, and others) became unavailable for several hours. This attack is considered one of the largest ever DDoS attacks, exceeding a rate of **1 Tbit/s**

| Misconfiguration                       | What It Enables                                                       |
| -------------------------------------- | --------------------------------------------------------------------- |
| `allow-query { any; }` on the resolver | Attacker can send queries to the resolver from anywhere               |
| Query type `ANY` allowed               | `ANY` queries produce the largest responses, maximizing amplification |
| **No rate limiting** (RRL)             | Resolver processes unlimited queries, amplifying the attack           |
| No source IP verification (BCP 38)     | Attacker can spoof source IPs without being blocked                   |

## Mitigations for Administrators

1. **Restrict recursion**: Only allow recursive queries from trusted clients.

2. **Implement Response Rate Limiting (RRL)**: Limits the number of identical responses sent to a single client.

3. **Disable `ANY` queries**: `RFC 8482` recommends returning minimal-sized responses for `ANY` queries.

4. **Source IP verification (BCP 38)**: ISPs should reject DNS traffic with spoofed addresses.

5. **Use anycast DNS and DDoS scrubbing services**: Distributes the load and filters malicious traffic.
